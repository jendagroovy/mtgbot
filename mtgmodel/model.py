import attr
from typing import List, Dict, Optional, Any

from .adapters import ServatriceAdapter


@attr.s
class Card:
    id = attr.ib()
    name = attr.ib()
    info = attr.ib()

    tapped = attr.ib(False)


@attr.s
class DeckData:
    """Data structure representing a Magic: The Gathering deck."""
    name = attr.ib(default="")
    description = attr.ib(default="")
    cards = attr.ib(factory=list)  # List of card objects with full info
    sideboard = attr.ib(factory=list)  # List of card objects with full info

    @classmethod
    def from_json(cls, json_data: Dict) -> 'DeckData':
        """Create a DeckData instance from a JSON-like dictionary.
        
        Args:
            json_data: Dictionary with deck data in the format:
                {
                    "data": {
                        "name": str,
                        "mainBoard": List[Dict[str, Any]],  # List of card objects with full info
                        "sideBoard": List[Dict[str, Any]]  # List of card objects with full info
                    }
                }
        """
        data = json_data.get("data", {})
        return cls(
            name=data.get("name", ""),
            description="",  # Description not present in current format
            cards=data.get("mainBoard", []),
            sideboard=data.get("sideBoard", [])
        )

    def get_card_info(self, card_name: str) -> Dict:
        """Get full card info for a given card name."""
        # Search in main deck
        for card in self.cards:
            if card["name"] == card_name:
                return card
        # Search in sideboard
        for card in self.sideboard:
            if card["name"] == card_name:
                return card
        return {}


@attr.s
class GameModel:
    """Game model for Magic: The Gathering."""

    adapter = attr.ib(None)
    deck = attr.ib(None, init=False)  # Changed from {} to None

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
        self.adapter.select_deck(deck)

    def card_drawn(self, card_id, card_name):
        self.hand.append(
            Card(id=card_id, name=card_name, info=self.deck.get_card_info(card_name))
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
            try:
                if card.info["types"][0] == 'Land':
                    lands.append(card)
            except KeyError:
                print(f"Card {card.name} has no types")
                import pdb; pdb.set_trace()

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
