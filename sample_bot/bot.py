from collections import defaultdict
from mtgmodel import GameModel
from stclient import ServatriceClient
import json
import time


class Bot:
    def __init__(self):
        self.client = self.initialize_client()
        self.game = GameModel.with_servatrice(client=self.client)

    @staticmethod
    def initialize_client():
        client = ServatriceClient(host="127.0.0.1", port=4747)

        client.connect()
        client.login(user_name="Bot", password="")
        client.join_room(0);

        if len(client.game_list) > 0:
            client.join_game(client.game_list[0].game_id)
            print("Joined game")
        else:
            client.create_game(
                description="Simulation",
                max_players=2,
                spectators_allowed=True,
                spectators_see_everything=True
            )
            print("Created game")

        return client

    def find_lands_to_pay_for(self, card_to_play):
        lands = []
        lands_by_color = defaultdict(list)
        selected_lands = []

        for card in self.game.table:
            if not card.tapped and card.info["types"][0] == 'Land':
                lands.append(card)
                for color in card.info["colorIdentity"]:
                    lands_by_color[color].append(card)

        costs = card_to_play.info["manaCost"].strip("{}").split("}{")

        # allocate particular color costs
        for cost in costs:
            if cost not in ["R", "W", "G", "U", "B"]:
                continue

            try:
                selected_land = lands_by_color[cost].pop()
            except IndexError:
                return None

            selected_lands.append(selected_land)
            lands.remove(selected_land)

        # allocate dual color costs
        for cost in costs:
            if '/' not in cost:
                continue

            selected_land = None
            for color in cost.split('/'):
                try:
                    selected_land = lands_by_color[color].pop()
                except IndexError:
                    pass

            if selected_land is None:
                return None

            selected_lands.append(selected_land)
            lands.remove(selected_land)

        # allocate color-less costs
        for cost in costs:
            if not cost.isnumeric():
                continue

            try:
                for num in range(0, int(cost)):
                    selected_lands.append(lands.pop())
            except IndexError:
                return None

        # If we reached here, we can afford to play the card :)
        return selected_lands

    def run(self):
        # Load deck json
        with open("Might.json") as fp:
            deck_json = json.load(fp)
        deck = {card["name"]: card for card in deck_json["mainBoard"]}

        game = self.game

        game.select_deck(deck)
        game.ready()
        game.wait(lambda: game.is_started)

        game.draw_cards(7)

        while not game.is_finished:
            # Wait for player's turn
            game.wait(lambda: game.active_player_id == game.player_id)

            # Cycle game phases
            for phase in range(0, 11):
                game.set_active_phase(phase)

                # Wait until the phase has been changed
                game.wait(lambda: game.active_phase == phase)

                if phase == 0:
                    # Untap cards
                    for card in game.table:
                        if card.tapped:
                            game.tap_card(card, False)

                if phase == 2:
                    # Draw card in Draw phase
                    game.draw_cards(1)

                if phase == 3:
                    # Play a land in Main phase
                    lands = game.find_lands()
                    if lands:
                        game.play_card(lands[0])

                    # Try to play a creature
                    creatures = game.find_creatures()
                    for creature in creatures:
                        lands = self.find_lands_to_pay_for(creature)
                        if lands is not None:
                            for land in lands:
                                game.tap_card(land)
                            game.play_card(creature)

                time.sleep(0.2)

            game.next_turn()

            # Wait until it's other player's turn
            game.wait(lambda: game.active_player_id != game.player_id)

