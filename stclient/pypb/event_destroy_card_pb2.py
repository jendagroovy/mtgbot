# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event_destroy_card.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import game_event_pb2 as game__event__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='event_destroy_card.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x18\x65vent_destroy_card.proto\x1a\x10game_event.proto\"e\n\x11\x45vent_DestroyCard\x12\x11\n\tzone_name\x18\x01 \x01(\t\x12\x0f\n\x07\x63\x61rd_id\x18\x02 \x01(\r2,\n\x03\x65xt\x12\n.GameEvent\x18\xdb\x0f \x01(\x0b\x32\x12.Event_DestroyCard')
  ,
  dependencies=[game__event__pb2.DESCRIPTOR,])




_EVENT_DESTROYCARD = _descriptor.Descriptor(
  name='Event_DestroyCard',
  full_name='Event_DestroyCard',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='zone_name', full_name='Event_DestroyCard.zone_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='card_id', full_name='Event_DestroyCard.card_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Event_DestroyCard.ext', index=0,
      number=2011, type=11, cpp_type=10, label=1,
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
  serialized_start=46,
  serialized_end=147,
)

DESCRIPTOR.message_types_by_name['Event_DestroyCard'] = _EVENT_DESTROYCARD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Event_DestroyCard = _reflection.GeneratedProtocolMessageType('Event_DestroyCard', (_message.Message,), dict(
  DESCRIPTOR = _EVENT_DESTROYCARD,
  __module__ = 'event_destroy_card_pb2'
  # @@protoc_insertion_point(class_scope:Event_DestroyCard)
  ))
_sym_db.RegisterMessage(Event_DestroyCard)

_EVENT_DESTROYCARD.extensions_by_name['ext'].message_type = _EVENT_DESTROYCARD
game__event__pb2.GameEvent.RegisterExtension(_EVENT_DESTROYCARD.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
