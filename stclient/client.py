import attr
from datetime import datetime
from collections import defaultdict
import json
import logging
import logging.config
import socket
import struct
import time

from .pypb import (
    CommandContainer,

    Command_Ping, Command_Login,
    Command_JoinRoom, Response_JoinRoom, Command_JoinGame, Command_CreateGame,
    Command_DeckSelect, Command_DrawCards, Command_MoveCard, Command_ReadyStart,
    Command_SetActivePhase, Command_NextTurn, Command_SetCardAttr,

    Event_GameJoined, Event_GameStateChanged, Event_SetActivePhase,
    Event_SetActivePlayer, Event_DrawCards,

    CardAttribute,

    ServerMessage
)

from .extension_mapping import COMMAND_EXTENSION_MAP


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

# Load Cockatrice deck
DECK_COCKATRICE = "<?xml version=\"1.0\"?><cockatrice_deck version=\"1\"><deckname></deckname><comments></comments><zone name=\"main\"><card number=\"1\" name=\"Lovisa Coldeyes\"/><card number=\"2\" name=\"Skarrgan Pit-Skulk\"/><card number=\"2\" name=\"Kruin Striker\"/><card number=\"1\" name=\"Talara\'s Battalion\"/><card number=\"1\" name=\"Radha, Heir to Keld\"/><card number=\"2\" name=\"Burning-Tree Emissary\"/><card number=\"1\" name=\"Zo-Zu the Punisher\"/><card number=\"1\" name=\"Relentless Hunter\"/><card number=\"2\" name=\"Ambassador Oak\"/><card number=\"2\" name=\"Gorehorn Minotaurs\"/><card number=\"2\" name=\"Cloudcrown Oak\"/><card number=\"1\" name=\"Rubblebelt Raiders\"/><card number=\"1\" name=\"Kamahl, Pit Fighter\"/><card number=\"1\" name=\"Boldwyr Intimidator\"/><card number=\"2\" name=\"Firebolt\"/><card number=\"2\" name=\"Rampant Growth\"/><card number=\"2\" name=\"Call of the Herd\"/><card number=\"1\" name=\"Harmonize\"/><card number=\"1\" name=\"Increasing Savagery\"/><card number=\"1\" name=\"Roar of the Wurm\"/><card number=\"1\" name=\"Guttural Response\"/><card number=\"2\" name=\"Sylvan Might\"/><card number=\"1\" name=\"Beacon of Destruction\"/><card number=\"1\" name=\"Beast Attack\"/><card number=\"1\" name=\"Coat of Arms\"/><card number=\"4\" name=\"Rugged Highlands\"/><card number=\"11\" name=\"Mountain\"/><card number=\"10\" name=\"Forest\"/></zone></cockatrice_deck>\n"


class NoDataReceived(Exception):
    pass


@attr.s
class ServatriceClient:

    host = attr.ib()
    port = attr.ib()

    sock = attr.ib(None, init=False)

    cmd_counter = attr.ib(0, init=False)

    game_list = attr.ib(None, init=False)
    game_id = attr.ib(None, init=False)
    game_info = attr.ib(None, init=False)
    player_id = attr.ib(None, init=False)


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
                self.emit_state_changed(
                    game_started=event_gamestatechanged.game_started,
                    player_id=self.player_id
                )

            elif event.HasExtension(Event_SetActivePhase.ext):
                event_setactivephase = event.Extensions[Event_SetActivePhase.ext]
                self.emit_set_active_phase(phase=event_setactivephase.phase)

            elif event.HasExtension(Event_SetActivePlayer.ext):
                event_setactiveplayer = event.Extensions[Event_SetActivePlayer.ext]
                self.emit_set_active_player_id(player_id=event_setactiveplayer.active_player_id)

            elif event.HasExtension(Event_DrawCards.ext):
                event_drawcards = event.Extensions[Event_DrawCards.ext]
                self.emit_draw_card(cards=event_drawcards.cards)

    def emit_draw_card(self, card):
        pass

    def emit_set_active_player_id(self, player_id):
        pass

    def emit_set_active_phase(self, phase):
        pass

    def emit_state_changed(self, game_started, player_id):
        pass

    def wait(self, check_condition):
        log.info("Waiting on condition")
        last_ping = datetime.now()
        while not check_condition():
            try:
                self.recv()
            except NoDataReceived:
                pass

            if datetime.now().timestamp() - last_ping.timestamp() > 4:
                cmd_ping = Command_Ping()
                self.send_command(cmd_ping, silent=True)
                self.recv(silent=True)
                last_ping = datetime.now()

            time.sleep(0.5)

    def login(self, user_name, password):
        cmd_login = Command_Login()
        cmd_login.user_name = user_name
        cmd_login.password = password
        cmd_login.clientid = "MtG Bot"
        cmd_login.clientver = "1.0"

        self.send_command(cmd_login)
        self.recv()

    def join_room(self, room_id):
        cmd_joinroom = Command_JoinRoom()
        cmd_joinroom.room_id = 0

        self.send_command(cmd_joinroom)
        response = self.recv(response_type=Response_JoinRoom)
        self.game_list = response.room_info.game_list

    def join_game(self, game_id):
        cmd_joingame = Command_JoinGame()
        cmd_joingame.game_id = game_id
        self.send_command(cmd_joingame)
        self.recv()
        self.game_id = cmd_joingame.game_id
        # Process GameJoined event
        cmd_ping = Command_Ping()
        self.send_command(cmd_ping)
        self.recv()

    def create_game(self, description, max_players=2, spectators_allowed=True, spectators_see_everything=True):
        cmd_creategame = Command_CreateGame()
        cmd_creategame.description = description
        cmd_creategame.max_players = max_players
        cmd_creategame.spectators_allowed = spectators_allowed
        cmd_creategame.spectators_see_everything = spectators_see_everything
        self.send_command(cmd_creategame)
        self.recv()
        # Process GameJoined event
        cmd_ping = Command_Ping()
        self.send_command(cmd_ping)
        self.recv()

    def select_deck(self):
        cmd_deckselect = Command_DeckSelect()
        cmd_deckselect.deck = DECK_COCKATRICE
        self.send_command(cmd_deckselect)
        self.recv()

    def ready(self):
        cmd_readystart = Command_ReadyStart()
        cmd_readystart.ready = 1
        self.send_command(cmd_readystart)
        self.recv()

    def draw_cards(self, number):
        cmd_drawcards = Command_DrawCards()
        cmd_drawcards.number = number
        self.send_command(cmd_drawcards)
        self.recv()

    def set_active_phase(self, phase):
        cmd_setactivephase = Command_SetActivePhase()
        cmd_setactivephase.phase = phase
        self.send_command(cmd_setactivephase)

    def next_turn(self):
        cmd_nextturn = Command_NextTurn()
        self.send_command(cmd_nextturn)

    def play_card(self, card_id, target_zone, target_row):
        cmd_movecard = Command_MoveCard()
        cmd_movecard.start_zone = "hand"
        cmd_movecard.start_player_id = self.player_id
        cmd_movecard.target_player_id = self.player_id
        cmd_movecard.target_zone = target_zone
        cmd_movecard.y = target_row
        card_to_move = cmd_movecard.cards_to_move.card.add()
        card_to_move.card_id = card_id
        self.send_command(cmd_movecard)
        self.recv()

    def tap_card(self, card_id, set_tapped=True):
        cmd_setcardattr = Command_SetCardAttr()
        cmd_setcardattr.attribute = CardAttribute.AttrTapped
        cmd_setcardattr.attr_value = "1" if set_tapped else "0"
        cmd_setcardattr.card_id = card_id
        cmd_setcardattr.zone = "table"
        self.send_command(cmd_setcardattr)
        self.recv()
