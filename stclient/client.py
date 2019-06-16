import attr
from contextlib import contextmanager
import logging
import logging.config
import socket
import struct
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
from pypb.commands_pb2 import CommandContainer
from pypb.event_server_identification_pb2 import Event_ServerIdentification
from pypb.response_pb2 import Response
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


@attr.s
class Client:

    host = attr.ib()
    port = attr.ib()

    sock = attr.ib(None, init=False)

    cmd_counter = attr.ib(0, init=False)

    def connect(self):
        log.info("connect")
        self.sock = socket.socket()
        self.sock.connect((self.host, self.port))
        print(self.sock.recv(60))

        # hack for old xml clients - server expects this and discards first message
        log.info("dummy command")
        empty_cmd = CommandContainer().SerializeToString()
        self.send_msg(empty_cmd)
        log.info("read reply")
        self.recv()

    def recv(self):
        log.info("read reply")
        header = self.sock.recv(4)
        msg_size = struct.unpack('>I', header)[0]
        raw_msg = self.sock.recv(msg_size)
        response = ServerMessage()
        response.ParseFromString(bytes(raw_msg))
        print(response)
        return response

    def send_command(self, command):
        log.info("send command")

        container = CommandContainer()

        command_type = COMMAND_EXTENSION_MAP[command.DESCRIPTOR]
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

        print(container)
        self.send_msg(container.SerializeToString())

    def send_msg(self, message):
        length_binary = struct.pack('>I', len(message))
        self.sock.sendall(length_binary)
        self.sock.sendall(message)


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
    client.recv()

    cmd_joinroom = Command_JoinRoom()
    cmd_joinroom.room_id = 0;

    client.send_command(cmd_joinroom)
    response_container = client.recv()
    response = response_container.response.Extensions[Response_JoinRoom.ext]
    game_count = response.room_info.game_count
    game_list = response.room_info.game_list

    if game_count > 0:
        pass


