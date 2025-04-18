# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: command_replay_download.proto

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
  name='command_replay_download.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1d\x63ommand_replay_download.proto\x1a\x16session_commands.proto\"g\n\x16\x43ommand_ReplayDownload\x12\x15\n\treplay_id\x18\x01 \x01(\x11:\x02-126\n\x03\x65xt\x12\x0f.SessionCommand\x18\xcd\x08 \x01(\x0b\x32\x17.Command_ReplayDownload')
  ,
  dependencies=[session__commands__pb2.DESCRIPTOR,])




_COMMAND_REPLAYDOWNLOAD = _descriptor.Descriptor(
  name='Command_ReplayDownload',
  full_name='Command_ReplayDownload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='replay_id', full_name='Command_ReplayDownload.replay_id', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Command_ReplayDownload.ext', index=0,
      number=1101, type=11, cpp_type=10, label=1,
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
  serialized_start=57,
  serialized_end=160,
)

DESCRIPTOR.message_types_by_name['Command_ReplayDownload'] = _COMMAND_REPLAYDOWNLOAD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Command_ReplayDownload = _reflection.GeneratedProtocolMessageType('Command_ReplayDownload', (_message.Message,), dict(
  DESCRIPTOR = _COMMAND_REPLAYDOWNLOAD,
  __module__ = 'command_replay_download_pb2'
  # @@protoc_insertion_point(class_scope:Command_ReplayDownload)
  ))
_sym_db.RegisterMessage(Command_ReplayDownload)

_COMMAND_REPLAYDOWNLOAD.extensions_by_name['ext'].message_type = _COMMAND_REPLAYDOWNLOAD
session__commands__pb2.SessionCommand.RegisterExtension(_COMMAND_REPLAYDOWNLOAD.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
