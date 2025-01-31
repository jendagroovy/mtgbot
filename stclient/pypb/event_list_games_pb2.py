# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event_list_games.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import room_event_pb2 as room__event__pb2
from . import serverinfo_game_pb2 as serverinfo__game__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='event_list_games.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x16\x65vent_list_games.proto\x1a\x10room_event.proto\x1a\x15serverinfo_game.proto\"b\n\x0f\x45vent_ListGames\x12#\n\tgame_list\x18\x01 \x03(\x0b\x32\x10.ServerInfo_Game2*\n\x03\x65xt\x12\n.RoomEvent\x18\xeb\x07 \x01(\x0b\x32\x10.Event_ListGames')
  ,
  dependencies=[room__event__pb2.DESCRIPTOR,serverinfo__game__pb2.DESCRIPTOR,])




_EVENT_LISTGAMES = _descriptor.Descriptor(
  name='Event_ListGames',
  full_name='Event_ListGames',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='game_list', full_name='Event_ListGames.game_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Event_ListGames.ext', index=0,
      number=1003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=165,
)

_EVENT_LISTGAMES.fields_by_name['game_list'].message_type = serverinfo__game__pb2._SERVERINFO_GAME
DESCRIPTOR.message_types_by_name['Event_ListGames'] = _EVENT_LISTGAMES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Event_ListGames = _reflection.GeneratedProtocolMessageType('Event_ListGames', (_message.Message,), dict(
  DESCRIPTOR = _EVENT_LISTGAMES,
  __module__ = 'event_list_games_pb2'
  # @@protoc_insertion_point(class_scope:Event_ListGames)
  ))
_sym_db.RegisterMessage(Event_ListGames)

_EVENT_LISTGAMES.extensions_by_name['ext'].message_type = _EVENT_LISTGAMES
room__event__pb2.RoomEvent.RegisterExtension(_EVENT_LISTGAMES.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
