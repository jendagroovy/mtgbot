# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: command_set_card_attr.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import game_commands_pb2 as game__commands__pb2
from . import card_attributes_pb2 as card__attributes__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='command_set_card_attr.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1b\x63ommand_set_card_attr.proto\x1a\x13game_commands.proto\x1a\x15\x63\x61rd_attributes.proto\"\xa1\x01\n\x13\x43ommand_SetCardAttr\x12\x0c\n\x04zone\x18\x01 \x01(\t\x12\x13\n\x07\x63\x61rd_id\x18\x02 \x01(\x11:\x02-1\x12!\n\tattribute\x18\x03 \x01(\x0e\x32\x0e.CardAttribute\x12\x12\n\nattr_value\x18\x04 \x01(\t20\n\x03\x65xt\x12\x0c.GameCommand\x18\xf5\x07 \x01(\x0b\x32\x14.Command_SetCardAttr')
  ,
  dependencies=[game__commands__pb2.DESCRIPTOR,card__attributes__pb2.DESCRIPTOR,])




_COMMAND_SETCARDATTR = _descriptor.Descriptor(
  name='Command_SetCardAttr',
  full_name='Command_SetCardAttr',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='zone', full_name='Command_SetCardAttr.zone', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='card_id', full_name='Command_SetCardAttr.card_id', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attribute', full_name='Command_SetCardAttr.attribute', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attr_value', full_name='Command_SetCardAttr.attr_value', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Command_SetCardAttr.ext', index=0,
      number=1013, type=11, cpp_type=10, label=1,
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
  serialized_start=76,
  serialized_end=237,
)

_COMMAND_SETCARDATTR.fields_by_name['attribute'].enum_type = card__attributes__pb2._CARDATTRIBUTE
DESCRIPTOR.message_types_by_name['Command_SetCardAttr'] = _COMMAND_SETCARDATTR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Command_SetCardAttr = _reflection.GeneratedProtocolMessageType('Command_SetCardAttr', (_message.Message,), dict(
  DESCRIPTOR = _COMMAND_SETCARDATTR,
  __module__ = 'command_set_card_attr_pb2'
  # @@protoc_insertion_point(class_scope:Command_SetCardAttr)
  ))
_sym_db.RegisterMessage(Command_SetCardAttr)

_COMMAND_SETCARDATTR.extensions_by_name['ext'].message_type = _COMMAND_SETCARDATTR
game__commands__pb2.GameCommand.RegisterExtension(_COMMAND_SETCARDATTR.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
