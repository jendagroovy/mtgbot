# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: command_create_token.proto

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
  name='command_create_token.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1a\x63ommand_create_token.proto\x1a\x13game_commands.proto\"\xfe\x01\n\x13\x43ommand_CreateToken\x12\x0c\n\x04zone\x18\x01 \x01(\t\x12\x11\n\tcard_name\x18\x02 \x01(\t\x12\r\n\x05\x63olor\x18\x03 \x01(\t\x12\n\n\x02pt\x18\x04 \x01(\t\x12\x12\n\nannotation\x18\x05 \x01(\t\x12\x1e\n\x16\x64\x65stroy_on_zone_change\x18\x06 \x01(\x08\x12\t\n\x01x\x18\x07 \x01(\x11\x12\t\n\x01y\x18\x08 \x01(\x11\x12\x13\n\x0btarget_zone\x18\t \x01(\t\x12\x1a\n\x0etarget_card_id\x18\n \x01(\x11:\x02-120\n\x03\x65xt\x12\x0c.GameCommand\x18\xf2\x07 \x01(\x0b\x32\x14.Command_CreateToken')
  ,
  dependencies=[game__commands__pb2.DESCRIPTOR,])




_COMMAND_CREATETOKEN = _descriptor.Descriptor(
  name='Command_CreateToken',
  full_name='Command_CreateToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='zone', full_name='Command_CreateToken.zone', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='card_name', full_name='Command_CreateToken.card_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color', full_name='Command_CreateToken.color', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pt', full_name='Command_CreateToken.pt', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='annotation', full_name='Command_CreateToken.annotation', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='destroy_on_zone_change', full_name='Command_CreateToken.destroy_on_zone_change', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='x', full_name='Command_CreateToken.x', index=6,
      number=7, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='Command_CreateToken.y', index=7,
      number=8, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_zone', full_name='Command_CreateToken.target_zone', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_card_id', full_name='Command_CreateToken.target_card_id', index=9,
      number=10, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Command_CreateToken.ext', index=0,
      number=1010, type=11, cpp_type=10, label=1,
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
  serialized_start=52,
  serialized_end=306,
)

DESCRIPTOR.message_types_by_name['Command_CreateToken'] = _COMMAND_CREATETOKEN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Command_CreateToken = _reflection.GeneratedProtocolMessageType('Command_CreateToken', (_message.Message,), dict(
  DESCRIPTOR = _COMMAND_CREATETOKEN,
  __module__ = 'command_create_token_pb2'
  # @@protoc_insertion_point(class_scope:Command_CreateToken)
  ))
_sym_db.RegisterMessage(Command_CreateToken)

_COMMAND_CREATETOKEN.extensions_by_name['ext'].message_type = _COMMAND_CREATETOKEN
game__commands__pb2.GameCommand.RegisterExtension(_COMMAND_CREATETOKEN.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
