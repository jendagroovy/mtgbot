import attr
from contextlib import contextmanager
import logging
import logging.config
import socket
import struct
from pypb.server_message_pb2 import ServerMessage
from pypb.session_commands_pb2 import Command_Register, Command_Ping, Command_Login, Command_ListRooms
from pypb.commands_pb2 import CommandContainer
from pypb.event_server_identification_pb2 import Event_ServerIdentification
from pypb.response_pb2 import Response

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


class CommandWrapper():

    def __init__(self, command_class):
        self._container = CommandContainer()
        session_command = self._container.session_command.add()
        self._command = session_command.Extensions[command_class.ext]
        self._command.Clear()

    def __getattr__(self, name):
        return getattr(self._command, name)

    def __setattr__(self, name, value):
        if name in ("_container", "_command"):
            super().__setattr__(name, value)
        else:
            setattr(self._command, name, value)


@attr.s
class Client():

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
        self.print_response(raw_msg)

    def print_response(self, resp):
        m = ServerMessage()
        m.ParseFromString(bytes(resp))
        print(m)

    def send_command(self, command):
        log.info("send command")

        container = CommandContainer()
        session_command = container.session_command.add()
        session_command.Extensions[command.ext].CopyFrom(command)

        #container = wrapped_command._container

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

    #cmd_login = CommandWrapper(Command_Login)
    cmd_login = Command_Login()
    cmd_login.user_name = "Bot"
    cmd_login.password = ""
    cmd_login.clientid = "MtG Bot"
    cmd_login.clientver = "1.0"


    client.send_command(cmd_login)
    client.recv()
    client.recv()

    #cmd_ping = CommandWrapper(Command_Ping)
    cmd_ping = Command_Ping()
    client.send_command(cmd_ping)
    client.recv()
    client.send_command(cmd_ping)
    client.recv()

    cmd_listrooms = Command_ListRooms()

    client.send_command(cmd_listrooms)
    client.recv()
