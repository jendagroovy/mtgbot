# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: command_replay_list.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import session_commands_pb2 as session__commands__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='command_replay_list.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x19\x63ommand_replay_list.proto\x1a\x16session_commands.proto\"H\n\x12\x43ommand_ReplayList22\n\x03\x65xt\x12\x0f.SessionCommand\x18\xcc\x08 \x01(\x0b\x32\x13.Command_ReplayList')
  ,
  dependencies=[session__commands__pb2.DESCRIPTOR,])




_COMMAND_REPLAYLIST = _descriptor.Descriptor(
  name='Command_ReplayList',
  full_name='Command_ReplayList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Command_ReplayList.ext', index=0,
      number=1100, type=11, cpp_type=10, label=1,
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
  serialized_start=53,
  serialized_end=125,
)

DESCRIPTOR.message_types_by_name['Command_ReplayList'] = _COMMAND_REPLAYLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Command_ReplayList = _reflection.GeneratedProtocolMessageType('Command_ReplayList', (_message.Message,), dict(
  DESCRIPTOR = _COMMAND_REPLAYLIST,
  __module__ = 'command_replay_list_pb2'
  # @@protoc_insertion_point(class_scope:Command_ReplayList)
  ))
_sym_db.RegisterMessage(Command_ReplayList)

_COMMAND_REPLAYLIST.extensions_by_name['ext'].message_type = _COMMAND_REPLAYLIST
session__commands__pb2.SessionCommand.RegisterExtension(_COMMAND_REPLAYLIST.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
