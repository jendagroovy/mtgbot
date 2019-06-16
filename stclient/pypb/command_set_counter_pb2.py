# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: command_set_counter.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import game_commands_pb2 as game__commands__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='command_set_counter.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x19\x63ommand_set_counter.proto\x1a\x13game_commands.proto\"l\n\x12\x43ommand_SetCounter\x12\x16\n\ncounter_id\x18\x01 \x01(\x11:\x02-1\x12\r\n\x05value\x18\x02 \x01(\x11\x32/\n\x03\x65xt\x12\x0c.GameCommand\x18\xfc\x07 \x01(\x0b\x32\x13.Command_SetCounter')
  ,
  dependencies=[game__commands__pb2.DESCRIPTOR,])




_COMMAND_SETCOUNTER = _descriptor.Descriptor(
  name='Command_SetCounter',
  full_name='Command_SetCounter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='counter_id', full_name='Command_SetCounter.counter_id', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='Command_SetCounter.value', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Command_SetCounter.ext', index=0,
      number=1020, type=11, cpp_type=10, label=1,
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
  serialized_start=50,
  serialized_end=158,
)

DESCRIPTOR.message_types_by_name['Command_SetCounter'] = _COMMAND_SETCOUNTER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Command_SetCounter = _reflection.GeneratedProtocolMessageType('Command_SetCounter', (_message.Message,), dict(
  DESCRIPTOR = _COMMAND_SETCOUNTER,
  __module__ = 'command_set_counter_pb2'
  # @@protoc_insertion_point(class_scope:Command_SetCounter)
  ))
_sym_db.RegisterMessage(Command_SetCounter)

_COMMAND_SETCOUNTER.extensions_by_name['ext'].message_type = _COMMAND_SETCOUNTER
game__commands__pb2.GameCommand.RegisterExtension(_COMMAND_SETCOUNTER.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
