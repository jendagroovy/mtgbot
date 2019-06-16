import attr
from datetime import datetime
from collections import defaultdict
import json
import logging
import logging.config
import socket
import struct
import time
from pypb.server_message_pb2 import ServerMessage
from pypb.session_commands_pb2 import (
    Command_Register, Command_Ping, Command_Login, Command_ListRooms,
    Command_JoinRoom
)
from pypb.response_join_room_pb2 import (
    Response_JoinRoom
)
from pypb.room_commands_pb2 import (
    Command_JoinGame, Command_CreateGame
)
from pypb.command_deck_select_pb2 import (
    Command_DeckSelect
)
from pypb.command_draw_cards_pb2 import (
    Command_DrawCards
)
from pypb.command_move_card_pb2 import (
    Command_MoveCard
)
from pypb.command_ready_start_pb2 import (
    Command_ReadyStart
)
from pypb.command_set_active_phase_pb2 import (
    Command_SetActivePhase
)
from pypb.command_next_turn_pb2 import (
    Command_NextTurn
)
from pypb.command_set_card_attr_pb2 import (
    Command_SetCardAttr
)
from pypb.event_game_joined_pb2 import (
    Event_GameJoined
)
from pypb.event_game_state_changed_pb2 import (
    Event_GameStateChanged
)
from pypb.event_set_active_phase_pb2 import (
    Event_SetActivePhase
)
from pypb.event_set_active_player_pb2 import (
    Event_SetActivePlayer
)
from pypb.event_draw_cards_pb2 import (
    Event_DrawCards
)
from pypb.card_attributes_pb2 import (
    CardAttribute
)
from pypb.commands_pb2 import CommandContainer
from pypb.event_server_identification_pb2 import Event_ServerIdentification
from pypb.response_pb2 import Response
from pypb.server_message_pb2 import ServerMessage
from pypb import COMMAND_EXTENSION_MAP

log = logging.getLogger(__name__)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'simple': {
            'format': '%(asctime)s [%(levelname)s] %(message)s'
        },
    },
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        __name__: {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
}
logging.config.dictConfig(LOGGING)


class NoDataReceived(Exception):
    pass


@attr.s
class Card:
    id = attr.ib()
    name = attr.ib()
    tapped = attr.ib(False)

    @property
    def info(self):
        return DECK[self.name]


@attr.s
class Client:

    host = attr.ib()
    port = attr.ib()

    sock = attr.ib(None, init=False)

    cmd_counter = attr.ib(0, init=False)

    game_info = attr.ib(None, init=False)
    game_started = attr.ib(False, init=False)
    player_id = attr.ib(None, init=False)

    active_phase = attr.ib(None, init=False)
    active_player_id = attr.ib(None, init=False)

    hand = attr.ib([], init=False)
    table = attr.ib([], init=False)

    def connect(self):
        log.info("connect")
        self.sock = socket.socket()
        self.sock.settimeout(0.5)
        self.sock.connect((self.host, self.port))
        print(self.sock.recv(60))

        # hack for old xml clients - server expects this and discards first message
        log.info("dummy command")
        empty_cmd = CommandContainer().SerializeToString()
        self.send_msg(empty_cmd)
        log.info("read reply")

    def recv(self, response_type=None, silent=False):
        while True:
            log.info("read reply")

            try:
                header = self.sock.recv(4)
            except socket.timeout:
                raise NoDataReceived()

            if header == b"":
                raise NoDataReceived()

            msg_size = struct.unpack('>I', header)[0]
            raw_msg = self.sock.recv(msg_size)
            server_message = ServerMessage()
            server_message.ParseFromString(bytes(raw_msg))
            if not silent:
                print(server_message)

            if server_message.message_type == ServerMessage.MessageType.SESSION_EVENT:
                self.handle_session_event(server_message)

            if server_message.message_type == ServerMessage.MessageType.GAME_EVENT_CONTAINER:
                self.handle_game_event(server_message)

            if server_message.message_type != ServerMessage.MessageType.RESPONSE:
                log.info("Ignoring message of type %s" % server_message.message_type)
                continue

            if response_type is None:
                return None

            response = server_message.response.Extensions[response_type.ext]

            return response

    def send_command(self, command, silent=False):
        log.info("send command")

        container = CommandContainer()

        command_type = COMMAND_EXTENSION_MAP[command.DESCRIPTOR]

        if command_type == 'GameCommand':
            if self.game_info is None:
                raise Exception("Can't send Game command outside of game")

            container.game_id = self.game_info.game_id

        command_field_map = {
            'SessionCommand': container.session_command,
            'GameCommand': container.game_command,
            'AdminCommand': container.admin_command,
            'ModeratorCommand': container.moderator_command,
            'RoomCommand': container.room_command
        }

        contained_command = command_field_map[command_type].add()
        contained_command.Extensions[command.ext].CopyFrom(command)

        container.cmd_id = self.cmd_counter
        self.cmd_counter += 1

        if not silent:
            print(container)
        self.send_msg(container.SerializeToString())

    def send_msg(self, message):
        length_binary = struct.pack('>I', len(message))
        self.sock.sendall(length_binary)
        self.sock.sendall(message)

    def handle_session_event(self, message):
        if message.session_event.HasExtension(Event_GameJoined.ext):
            event_gamejoined = message.session_event.Extensions[Event_GameJoined.ext]
            self.game_info = event_gamejoined.game_info
            self.player_id = event_gamejoined.player_id
            log.info("Entered game: %s" % event_gamejoined.game_info.game_id)

    def handle_game_event(self, message):
        for event in message.game_event_container.event_list:
            log.info("Received game event")

            if event.HasExtension(Event_GameStateChanged.ext):
                event_gamestatechanged = event.Extensions[Event_GameStateChanged.ext]
                self.game_started = event_gamestatechanged.game_started
                log.info("Game has started")

            elif event.HasExtension(Event_SetActivePhase.ext):
                event_setactivephase = event.Extensions[Event_SetActivePhase.ext]
                self.active_phase = event_setactivephase.phase
                log.info("Active phase is %s" % self.active_phase)

            elif event.HasExtension(Event_SetActivePlayer.ext):
                event_setactiveplayer = event.Extensions[Event_SetActivePlayer.ext]
                self.active_player_id = event_setactiveplayer.active_player_id
                log.info("It's turn of player %s" % self.active_player_id)

            elif event.HasExtension(Event_DrawCards.ext):
                event_drawcards = event.Extensions[Event_DrawCards.ext]
                for card in event_drawcards.cards:
                    self.hand.append(Card(id=card.id, name=card.name))

    def wait(self, check_condition):
        log.info("Waiting on condition")
        last_ping = datetime.now()
        while not check_condition():
            try:
                client.recv()
            except NoDataReceived:
                pass

            if datetime.now().timestamp() - last_ping.timestamp() > 4:
                cmd_ping = Command_Ping()
                client.send_command(cmd_ping, silent=True)
                client.recv(silent=True)
                last_ping = datetime.now()

            time.sleep(0.5)


def find_land(hand):
    for card in hand:
        if card.info["types"][0] == 'Land':
            return card

    return None

def find_creatures(hand):
    creatures = []
    for card in hand:
        if card.info["types"][0] == 'Creature':
            creatures.append(card)

    return creatures

def find_lands_to_pay_for(card_to_play, table):
    lands = []
    lands_by_color = defaultdict(list)
    selected_lands = []

    for card in table:
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

        try:
            selected_lands.append(selected_land)
            lands.remove(selected_land)
        except:
            import pdb; pdb.set_trace()

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

        try:
            selected_lands.append(selected_land)
            lands.remove(selected_land)
        except:
            import pdb; pdb.set_trace()

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


def play_card(card):
    cmd_movecard = Command_MoveCard()
    cmd_movecard.start_zone = "hand"
    cmd_movecard.start_player_id = client.player_id
    cmd_movecard.target_player_id = client.player_id
    if card.info["types"][0] == 'Land':
        cmd_movecard.target_zone = "table"
        cmd_movecard.y = 2
    else:
        cmd_movecard.target_zone = "stack"
    card_to_move = cmd_movecard.cards_to_move.card.add()
    card_to_move.card_id = card.id
    client.send_command(cmd_movecard)
    client.recv()
    client.hand.remove(card)
    client.table.append(card)

def tap_card(card, set_tapped=True):
    cmd_setcardattr = Command_SetCardAttr()
    cmd_setcardattr.attribute = CardAttribute.AttrTapped
    cmd_setcardattr.attr_value = "1" if set_tapped else "0"
    cmd_setcardattr.card_id = card.id
    cmd_setcardattr.zone = "table"
    client.send_command(cmd_setcardattr)
    client.recv()
    card.tapped = set_tapped

    return


    cmd_movecard = Command_MoveCard()
    cmd_movecard.start_zone = "table"
    cmd_movecard.target_zone = "table"
    cmd_movecard.start_player_id = client.player_id
    cmd_movecard.target_player_id = client.player_id
    cmd_movecard.y = 2
    card_to_move = cmd_movecard.cards_to_move.card.add()
    card_to_move.card_id = card.id
    card_to_move.tapped = set_tapped
    client.send_command(cmd_movecard)
    client.recv()
    card.tapped = set_tapped

if __name__ == "__main__":
    client = Client(host="127.0.0.1", port=4747)

    client.connect()

    cmd_login = Command_Login()
    cmd_login.user_name = "Bot"
    cmd_login.password = ""
    cmd_login.clientid = "MtG Bot"
    cmd_login.clientver = "1.0"


    client.send_command(cmd_login)
    client.recv()

    cmd_joinroom = Command_JoinRoom()
    cmd_joinroom.room_id = 0;

    client.send_command(cmd_joinroom)
    response = client.recv(response_type=Response_JoinRoom)
    #response = response_container.response.Extensions[Response_JoinRoom.ext]
    game_count = response.room_info.game_count
    game_list = response.room_info.game_list

    game_id = None

    if game_count > 0:
        cmd_joingame = Command_JoinGame()
        cmd_joingame.game_id = game_list[0].game_id
        client.send_command(cmd_joingame)
        client.recv()
        game_id = cmd_joingame.game_id
        print("Joined game")
    else:
        cmd_creategame = Command_CreateGame()
        cmd_creategame.description = "Simulation"
        cmd_creategame.max_players = 2
        cmd_creategame.spectators_allowed = True
        cmd_creategame.spectators_see_everything = True
        client.send_command(cmd_creategame)
        response = client.recv()
        print("Created game")


    # Process GameJoined event
    cmd_ping = Command_Ping()
    client.send_command(cmd_ping)
    client.recv()

    # Load Cockatrice deck
    DECK_COCKATRICE = "<?xml version=\"1.0\"?><cockatrice_deck version=\"1\"><deckname></deckname><comments></comments><zone name=\"main\"><card number=\"1\" name=\"Lovisa Coldeyes\"/><card number=\"2\" name=\"Skarrgan Pit-Skulk\"/><card number=\"2\" name=\"Kruin Striker\"/><card number=\"1\" name=\"Talara\'s Battalion\"/><card number=\"1\" name=\"Radha, Heir to Keld\"/><card number=\"2\" name=\"Burning-Tree Emissary\"/><card number=\"1\" name=\"Zo-Zu the Punisher\"/><card number=\"1\" name=\"Relentless Hunter\"/><card number=\"2\" name=\"Ambassador Oak\"/><card number=\"2\" name=\"Gorehorn Minotaurs\"/><card number=\"2\" name=\"Cloudcrown Oak\"/><card number=\"1\" name=\"Rubblebelt Raiders\"/><card number=\"1\" name=\"Kamahl, Pit Fighter\"/><card number=\"1\" name=\"Boldwyr Intimidator\"/><card number=\"2\" name=\"Firebolt\"/><card number=\"2\" name=\"Rampant Growth\"/><card number=\"2\" name=\"Call of the Herd\"/><card number=\"1\" name=\"Harmonize\"/><card number=\"1\" name=\"Increasing Savagery\"/><card number=\"1\" name=\"Roar of the Wurm\"/><card number=\"1\" name=\"Guttural Response\"/><card number=\"2\" name=\"Sylvan Might\"/><card number=\"1\" name=\"Beacon of Destruction\"/><card number=\"1\" name=\"Beast Attack\"/><card number=\"1\" name=\"Coat of Arms\"/><card number=\"4\" name=\"Rugged Highlands\"/><card number=\"11\" name=\"Mountain\"/><card number=\"10\" name=\"Forest\"/></zone></cockatrice_deck>\n"
    # Load deck json
    with open("Might.json") as fp:
        DECK_JSON = json.load(fp)
    DECK = {card["name"]: card for card in DECK_JSON["mainBoard"]}


    cmd_deckselect = Command_DeckSelect()
    cmd_deckselect.deck = DECK_COCKATRICE
    client.send_command(cmd_deckselect)
    client.recv()

    # Player is ready to start
    cmd_readystart = Command_ReadyStart()
    cmd_readystart.ready = 1
    client.send_command(cmd_readystart)
    client.recv()

    # Wait for game to start
    client.wait(lambda: client.game_started)

    # Draw initial hand
    cmd_drawcards = Command_DrawCards()
    cmd_drawcards.number = 7
    client.send_command(cmd_drawcards)
    client.recv()

    while True:
        # Wait for player's turn
        client.wait(lambda: client.active_player_id == client.player_id)

        # Cycle game phases
        for phase in range(0, 11):
            cmd_setactivephase = Command_SetActivePhase()
            cmd_setactivephase.phase = phase
            client.send_command(cmd_setactivephase)

            # Wait until the phase has been changed
            client.wait(lambda: client.active_phase == phase)

            if phase == 0:
                # Untap cards
                for card in client.table:
                    if card.tapped:
                        tap_card(card, False)

            if phase == 2:
                # Draw card in Draw phase
                cmd_drawcards = Command_DrawCards()
                cmd_drawcards.number = 1
                client.send_command(cmd_drawcards)
                client.recv()

            if phase == 3:
                # Play a land in Main phase
                land = find_land(client.hand)
                if land:
                    play_card(land)

                # Try to play a creature
                creatures = find_creatures(client.hand)
                for creature in creatures:
                    lands = find_lands_to_pay_for(creature, client.table)
                    if lands is not None:
                        for land in lands:
                            tap_card(land)
                        play_card(creature)
                        break  # Don't play more than one creature

            time.sleep(0.2)

        cmd_nextturn = Command_NextTurn()
        client.send_command(cmd_nextturn)

        # Wait until it's other player's turn
        client.wait(lambda: client.active_player_id != client.player_id)


    client.wait(lambda: False)

