import attr
from datetime import datetime
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
from pypb.command_ready_start_pb2 import (
    Command_ReadyStart
)
from pypb.event_game_joined_pb2 import (
    Event_GameJoined
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
class Client:

    host = attr.ib()
    port = attr.ib()

    sock = attr.ib(None, init=False)

    cmd_counter = attr.ib(0, init=False)

    game_info = attr.ib(None, init=False)

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
            log.info("Entered game: %s" % event_gamejoined.game_info.game_id)


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
    client.send_command(cmd_ping, silent=True)
    client.recv(silent=True)


    # Load deck
    DECK = "<?xml version=\"1.0\"?><cockatrice_deck version=\"1\"><deckname></deckname><comments></comments><zone name=\"main\"><card number=\"1\" name=\"Lovisa Coldeyes\"/><card number=\"2\" name=\"Skarrgan Pit-Skulk\"/><card number=\"2\" name=\"Kruin Striker\"/><card number=\"1\" name=\"Talara\'s Battalion\"/><card number=\"1\" name=\"Radha, Heir to Keld\"/><card number=\"2\" name=\"Burning-Tree Emissary\"/><card number=\"1\" name=\"Zo-Zu the Punisher\"/><card number=\"1\" name=\"Relentless Hunter\"/><card number=\"2\" name=\"Ambassador Oak\"/><card number=\"2\" name=\"Gorehorn Minotaurs\"/><card number=\"2\" name=\"Cloudcrown Oak\"/><card number=\"1\" name=\"Rubblebelt Raiders\"/><card number=\"1\" name=\"Kamahl, Pit Fighter\"/><card number=\"1\" name=\"Boldwyr Intimidator\"/><card number=\"2\" name=\"Firebolt\"/><card number=\"2\" name=\"Rampant Growth\"/><card number=\"2\" name=\"Call of the Herd\"/><card number=\"1\" name=\"Harmonize\"/><card number=\"1\" name=\"Increasing Savagery\"/><card number=\"1\" name=\"Roar of the Wurm\"/><card number=\"1\" name=\"Guttural Response\"/><card number=\"2\" name=\"Sylvan Might\"/><card number=\"1\" name=\"Beacon of Destruction\"/><card number=\"1\" name=\"Beast Attack\"/><card number=\"1\" name=\"Coat of Arms\"/><card number=\"4\" name=\"Rugged Highlands\"/><card number=\"11\" name=\"Mountain\"/><card number=\"10\" name=\"Forest\"/></zone></cockatrice_deck>\n"

    cmd_deckselect = Command_DeckSelect()
    cmd_deckselect.deck = DECK
    client.send_command(cmd_deckselect)
    client.recv()

    # Player is ready to start
    cmd_readystart = Command_ReadyStart()
    cmd_readystart.ready = 1
    client.send_command(cmd_readystart)
    client.recv()

    # Draw cards
    cmd_drawcards = Command_DrawCards()
    cmd_drawcards.number = 10
    client.send_command(cmd_drawcards)
    client.recv()


    last_ping = datetime.now()
    while True:
        try:
            client.recv()
        except NoDataReceived:
            pass

        if datetime.now().timestamp() - last_ping.timestamp() > 1:
            print("Sending ping")
            cmd_ping = Command_Ping()
            client.send_command(cmd_ping, silent=True)
            client.recv(silent=True)


