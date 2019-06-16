# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: command_create_counter.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import game_commands_pb2 as game__commands__pb2
from . import color_pb2 as color__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='command_create_counter.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1c\x63ommand_create_counter.proto\x1a\x13game_commands.proto\x1a\x0b\x63olor.proto\"\x9f\x01\n\x15\x43ommand_CreateCounter\x12\x14\n\x0c\x63ounter_name\x18\x01 \x01(\t\x12\x1d\n\rcounter_color\x18\x02 \x01(\x0b\x32\x06.color\x12\x0e\n\x06radius\x18\x03 \x01(\r\x12\r\n\x05value\x18\x04 \x01(\x11\x32\x32\n\x03\x65xt\x12\x0c.GameCommand\x18\xfb\x07 \x01(\x0b\x32\x16.Command_CreateCounter')
  ,
  dependencies=[game__commands__pb2.DESCRIPTOR,color__pb2.DESCRIPTOR,])




_COMMAND_CREATECOUNTER = _descriptor.Descriptor(
  name='Command_CreateCounter',
  full_name='Command_CreateCounter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='counter_name', full_name='Command_CreateCounter.counter_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='counter_color', full_name='Command_CreateCounter.counter_color', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='radius', full_name='Command_CreateCounter.radius', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='Command_CreateCounter.value', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Command_CreateCounter.ext', index=0,
      number=1019, type=11, cpp_type=10, label=1,
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
  serialized_end=226,
)

_COMMAND_CREATECOUNTER.fields_by_name['counter_color'].message_type = color__pb2._COLOR
DESCRIPTOR.message_types_by_name['Command_CreateCounter'] = _COMMAND_CREATECOUNTER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Command_CreateCounter = _reflection.GeneratedProtocolMessageType('Command_CreateCounter', (_message.Message,), dict(
  DESCRIPTOR = _COMMAND_CREATECOUNTER,
  __module__ = 'command_create_counter_pb2'
  # @@protoc_insertion_point(class_scope:Command_CreateCounter)
  ))
_sym_db.RegisterMessage(Command_CreateCounter)

_COMMAND_CREATECOUNTER.extensions_by_name['ext'].message_type = _COMMAND_CREATECOUNTER
game__commands__pb2.GameCommand.RegisterExtension(_COMMAND_CREATECOUNTER.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
