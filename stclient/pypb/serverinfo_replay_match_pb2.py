# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: serverinfo_replay_match.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import serverinfo_replay_pb2 as serverinfo__replay__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='serverinfo_replay_match.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1dserverinfo_replay_match.proto\x1a\x17serverinfo_replay.proto\"\xcd\x01\n\x16ServerInfo_ReplayMatch\x12\'\n\x0breplay_list\x18\x01 \x03(\x0b\x32\x12.ServerInfo_Replay\x12\x13\n\x07game_id\x18\x02 \x01(\x11:\x02-1\x12\x11\n\troom_name\x18\x03 \x01(\t\x12\x14\n\x0ctime_started\x18\x04 \x01(\r\x12\x0e\n\x06length\x18\x05 \x01(\r\x12\x11\n\tgame_name\x18\x06 \x01(\t\x12\x14\n\x0cplayer_names\x18\x07 \x03(\t\x12\x13\n\x0b\x64o_not_hide\x18\x08 \x01(\x08')
  ,
  dependencies=[serverinfo__replay__pb2.DESCRIPTOR,])




_SERVERINFO_REPLAYMATCH = _descriptor.Descriptor(
  name='ServerInfo_ReplayMatch',
  full_name='ServerInfo_ReplayMatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='replay_list', full_name='ServerInfo_ReplayMatch.replay_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='game_id', full_name='ServerInfo_ReplayMatch.game_id', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='room_name', full_name='ServerInfo_ReplayMatch.room_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_started', full_name='ServerInfo_ReplayMatch.time_started', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='length', full_name='ServerInfo_ReplayMatch.length', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='game_name', full_name='ServerInfo_ReplayMatch.game_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player_names', full_name='ServerInfo_ReplayMatch.player_names', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='do_not_hide', full_name='ServerInfo_ReplayMatch.do_not_hide', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
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
  serialized_start=59,
  serialized_end=264,
)

_SERVERINFO_REPLAYMATCH.fields_by_name['replay_list'].message_type = serverinfo__replay__pb2._SERVERINFO_REPLAY
DESCRIPTOR.message_types_by_name['ServerInfo_ReplayMatch'] = _SERVERINFO_REPLAYMATCH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServerInfo_ReplayMatch = _reflection.GeneratedProtocolMessageType('ServerInfo_ReplayMatch', (_message.Message,), dict(
  DESCRIPTOR = _SERVERINFO_REPLAYMATCH,
  __module__ = 'serverinfo_replay_match_pb2'
  # @@protoc_insertion_point(class_scope:ServerInfo_ReplayMatch)
  ))
_sym_db.RegisterMessage(ServerInfo_ReplayMatch)


# @@protoc_insertion_point(module_scope)
