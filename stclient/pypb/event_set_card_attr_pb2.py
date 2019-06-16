# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event_set_card_attr.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import game_event_pb2 as game__event__pb2
from . import card_attributes_pb2 as card__attributes__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='event_set_card_attr.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x19\x65vent_set_card_attr.proto\x1a\x10game_event.proto\x1a\x15\x63\x61rd_attributes.proto\"\x9c\x01\n\x11\x45vent_SetCardAttr\x12\x11\n\tzone_name\x18\x01 \x01(\t\x12\x0f\n\x07\x63\x61rd_id\x18\x02 \x01(\x11\x12!\n\tattribute\x18\x03 \x01(\x0e\x32\x0e.CardAttribute\x12\x12\n\nattr_value\x18\x04 \x01(\t2,\n\x03\x65xt\x12\n.GameEvent\x18\xde\x0f \x01(\x0b\x32\x12.Event_SetCardAttr')
  ,
  dependencies=[game__event__pb2.DESCRIPTOR,card__attributes__pb2.DESCRIPTOR,])




_EVENT_SETCARDATTR = _descriptor.Descriptor(
  name='Event_SetCardAttr',
  full_name='Event_SetCardAttr',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='zone_name', full_name='Event_SetCardAttr.zone_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='card_id', full_name='Event_SetCardAttr.card_id', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attribute', full_name='Event_SetCardAttr.attribute', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attr_value', full_name='Event_SetCardAttr.attr_value', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Event_SetCardAttr.ext', index=0,
      number=2014, type=11, cpp_type=10, label=1,
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
  serialized_start=71,
  serialized_end=227,
)

_EVENT_SETCARDATTR.fields_by_name['attribute'].enum_type = card__attributes__pb2._CARDATTRIBUTE
DESCRIPTOR.message_types_by_name['Event_SetCardAttr'] = _EVENT_SETCARDATTR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Event_SetCardAttr = _reflection.GeneratedProtocolMessageType('Event_SetCardAttr', (_message.Message,), dict(
  DESCRIPTOR = _EVENT_SETCARDATTR,
  __module__ = 'event_set_card_attr_pb2'
  # @@protoc_insertion_point(class_scope:Event_SetCardAttr)
  ))
_sym_db.RegisterMessage(Event_SetCardAttr)

_EVENT_SETCARDATTR.extensions_by_name['ext'].message_type = _EVENT_SETCARDATTR
game__event__pb2.GameEvent.RegisterExtension(_EVENT_SETCARDATTR.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
