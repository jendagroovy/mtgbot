# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event_server_identification.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import session_event_pb2 as session__event__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='event_server_identification.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n!event_server_identification.proto\x1a\x13session_event.proto\"\x9d\x01\n\x1a\x45vent_ServerIdentification\x12\x13\n\x0bserver_name\x18\x01 \x01(\t\x12\x16\n\x0eserver_version\x18\x02 \x01(\t\x12\x18\n\x10protocol_version\x18\x03 \x01(\r28\n\x03\x65xt\x12\r.SessionEvent\x18\xf4\x03 \x01(\x0b\x32\x1b.Event_ServerIdentification')
  ,
  dependencies=[session__event__pb2.DESCRIPTOR,])




_EVENT_SERVERIDENTIFICATION = _descriptor.Descriptor(
  name='Event_ServerIdentification',
  full_name='Event_ServerIdentification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_name', full_name='Event_ServerIdentification.server_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='server_version', full_name='Event_ServerIdentification.server_version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='protocol_version', full_name='Event_ServerIdentification.protocol_version', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Event_ServerIdentification.ext', index=0,
      number=500, type=11, cpp_type=10, label=1,
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
  serialized_start=59,
  serialized_end=216,
)

DESCRIPTOR.message_types_by_name['Event_ServerIdentification'] = _EVENT_SERVERIDENTIFICATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Event_ServerIdentification = _reflection.GeneratedProtocolMessageType('Event_ServerIdentification', (_message.Message,), dict(
  DESCRIPTOR = _EVENT_SERVERIDENTIFICATION,
  __module__ = 'event_server_identification_pb2'
  # @@protoc_insertion_point(class_scope:Event_ServerIdentification)
  ))
_sym_db.RegisterMessage(Event_ServerIdentification)

_EVENT_SERVERIDENTIFICATION.extensions_by_name['ext'].message_type = _EVENT_SERVERIDENTIFICATION
session__event__pb2.SessionEvent.RegisterExtension(_EVENT_SERVERIDENTIFICATION.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
