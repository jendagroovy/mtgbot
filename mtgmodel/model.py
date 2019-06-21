import attr

from .adapters import ServatriceAdapter


@attr.s
class Card:
    id = attr.ib()
    name = attr.ib()
    info = attr.ib()

    tapped = attr.ib(False)


@attr.s
class GameModel:

    adapter = attr.ib(None)

    deck = attr.ib({}, init=False)

    is_started = attr.ib(False,init=False)
    is_finished = attr.ib(False, init=False)

    active_player_id = attr.ib(None, init=False)
    active_phase = attr.ib(None, init=False)
    player_id = attr.ib(None, init=False)

    hand = attr.ib([], init=False)
    table = attr.ib([], init=False)

    def __attrs_post_init__(self):
        self.adapter.game = self

    @classmethod
    def with_servatrice(cls, client):
        adapter = ServatriceAdapter(client=client)
        return GameModel(adapter=adapter)

    def select_deck(self, deck):
        self.deck = deck
        self.adapter.select_deck()

    def card_drawn(self, card_id, card_name):
        self.hand.append(
            Card(id=card_id, name=card_name, info=self.deck[card_name])
        )

    def ready(self):
        self.adapter.ready()

    def set_active_phase(self, phase):
        self.adapter.set_active_phase(phase)

    def wait(self, check_condition):
        self.adapter.wait(check_condition)

    def draw_cards(self, number):
        self.adapter.draw_cards(number)

    def next_turn(self):
        self.adapter.next_turn()

    def find_lands(self):
        lands = []
        for card in self.hand:
            if card.info["types"][0] == 'Land':
                lands.append(card)

        return lands

    def find_creatures(self):
        creatures = []
        for card in self.hand:
            if card.info["types"][0] == 'Creature':
                creatures.append(card)

        return creatures

    def play_card(self, card):
        if card.info["types"][0] == 'Land':
            target_zone = "table"
            target_row = 2
        else:
            target_zone = "table"
            target_row = 0

        self.adapter.play_card(card.id, target_zone, target_row)
        self.hand.remove(card)
        self.table.append(card)

    def tap_card(self, card, set_tapped=True):
        self.adapter.tap_card(card.id, set_tapped)
        card.tapped = set_tapped
