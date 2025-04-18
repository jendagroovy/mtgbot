# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event_dump_zone.proto

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
  name='event_dump_zone.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x15\x65vent_dump_zone.proto\x1a\x10game_event.proto\"{\n\x0e\x45vent_DumpZone\x12\x15\n\rzone_owner_id\x18\x01 \x01(\x11\x12\x11\n\tzone_name\x18\x02 \x01(\t\x12\x14\n\x0cnumber_cards\x18\x03 \x01(\x11\x32)\n\x03\x65xt\x12\n.GameEvent\x18\xe2\x0f \x01(\x0b\x32\x0f.Event_DumpZone')
  ,
  dependencies=[game__event__pb2.DESCRIPTOR,])




_EVENT_DUMPZONE = _descriptor.Descriptor(
  name='Event_DumpZone',
  full_name='Event_DumpZone',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='zone_owner_id', full_name='Event_DumpZone.zone_owner_id', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zone_name', full_name='Event_DumpZone.zone_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='number_cards', full_name='Event_DumpZone.number_cards', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Event_DumpZone.ext', index=0,
      number=2018, type=11, cpp_type=10, label=1,
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
  serialized_start=43,
  serialized_end=166,
)

DESCRIPTOR.message_types_by_name['Event_DumpZone'] = _EVENT_DUMPZONE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Event_DumpZone = _reflection.GeneratedProtocolMessageType('Event_DumpZone', (_message.Message,), dict(
  DESCRIPTOR = _EVENT_DUMPZONE,
  __module__ = 'event_dump_zone_pb2'
  # @@protoc_insertion_point(class_scope:Event_DumpZone)
  ))
_sym_db.RegisterMessage(Event_DumpZone)

_EVENT_DUMPZONE.extensions_by_name['ext'].message_type = _EVENT_DUMPZONE
game__event__pb2.GameEvent.RegisterExtension(_EVENT_DUMPZONE.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
