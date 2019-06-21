from .pypb.session_commands_pb2 import SessionCommand
from .pypb.room_commands_pb2 import RoomCommand
from .pypb.game_commands_pb2 import GameCommand
from .pypb.moderator_commands_pb2 import ModeratorCommand
from .pypb.admin_commands_pb2 import AdminCommand


def construct_extension_mapping(message_types):
    mapping = {}

    for message_type in message_types:
        extensions = message_type.DESCRIPTOR.file.pool.FindAllExtensions(
            message_type.DESCRIPTOR
        )
        for extension in extensions:
            mapping[extension.extension_scope] = message_type.DESCRIPTOR.name

    return mapping


COMMAND_EXTENSION_MAP = construct_extension_mapping((
    SessionCommand, RoomCommand, GameCommand,
    ModeratorCommand, AdminCommand
))
