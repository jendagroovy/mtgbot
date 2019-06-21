from .server_message_pb2 import ServerMessage
from .session_commands_pb2 import (
    Command_Register, Command_Ping, Command_Login, Command_ListRooms,
    Command_JoinRoom
)
from .response_join_room_pb2 import (
    Response_JoinRoom
)
from .room_commands_pb2 import (
    Command_JoinGame, Command_CreateGame
)
from .command_deck_select_pb2 import (
    Command_DeckSelect
)
from .command_draw_cards_pb2 import (
    Command_DrawCards
)
from .command_move_card_pb2 import (
    Command_MoveCard
)
from .command_ready_start_pb2 import (
    Command_ReadyStart
)
from .command_set_active_phase_pb2 import (
    Command_SetActivePhase
)
from .command_next_turn_pb2 import (
    Command_NextTurn
)
from .command_set_card_attr_pb2 import (
    Command_SetCardAttr
)
from .event_game_joined_pb2 import (
    Event_GameJoined
)
from .event_game_state_changed_pb2 import (
    Event_GameStateChanged
)
from .event_set_active_phase_pb2 import (
    Event_SetActivePhase
)
from .event_set_active_player_pb2 import (
    Event_SetActivePlayer
)
from .event_draw_cards_pb2 import (
    Event_DrawCards
)
from .card_attributes_pb2 import (
    CardAttribute
)
from .commands_pb2 import CommandContainer
from .event_server_identification_pb2 import Event_ServerIdentification
from .response_pb2 import Response
from .server_message_pb2 import ServerMessage
from .game_commands_pb2 import GameCommand
from .moderator_commands_pb2 import ModeratorCommand
from .admin_commands_pb2 import AdminCommand

from .extension_mapping import construct_extension_mapping

COMMAND_EXTENSION_MAP = construct_extension_mapping((
    session_commands_pb2.SessionCommand,
    room_commands_pb2.RoomCommand,
    game_commands_pb2.GameCommand,
    moderator_commands_pb2.ModeratorCommand,
    admin_commands_pb2.AdminCommand
))
