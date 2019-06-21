import attr
import logging

from .base import GameAdapter


log = logging.getLogger()


@attr.s
class ServatriceAdapter(GameAdapter):
    client = attr.ib(None)
    game = attr.ib(None, init=False)

    def __attrs_post_init__(self):
        self.client.emit_state_changed = self.on_state_changed
        self.client.emit_set_active_phase = self.on_set_active_phase
        self.client.emit_set_active_player_id = self.on_set_active_player_id
        self.client.emit_draw_card = self.on_draw_card

    def on_state_changed(self, game_started, player_id):
        self.game.is_started = game_started
        self.game.player_id = player_id
        log.info("Game has started")

    def on_set_active_phase(self, phase):
        self.game.active_phase = phase
        log.info("Active phase is %s" % phase)

    def on_set_active_player_id(self, player_id):
        self.game.active_player_id = player_id
        log.info("It's turn of player %s" % player_id)

    def on_draw_card(self, cards):
        for card in cards:
            self.game.card_drawn(card_id=card.id, card_name=card.name)

    def select_deck(self):
        self.client.select_deck()

    def ready(self):
        self.client.ready()

    def set_active_phase(self, phase):
        self.client.set_active_phase(phase)

    def wait(self, check_condition):
        self.client.wait(check_condition)

    def draw_cards(self, number):
        self.client.draw_cards(number)

    def next_turn(self):
        self.client.next_turn()

    def play_card(self, card_id, target_zone, target_row):
        self.client.play_card(card_id, target_zone, target_row)

    def tap_card(self, card_id, set_tapped=True):
        self.client.tap_card(card_id, set_tapped)
