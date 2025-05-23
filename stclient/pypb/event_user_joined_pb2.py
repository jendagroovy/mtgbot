# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event_user_joined.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import session_event_pb2 as session__event__pb2
from . import serverinfo_user_pb2 as serverinfo__user__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='event_user_joined.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x17\x65vent_user_joined.proto\x1a\x13session_event.proto\x1a\x15serverinfo_user.proto\"g\n\x10\x45vent_UserJoined\x12#\n\tuser_info\x18\x01 \x01(\x0b\x32\x10.ServerInfo_User2.\n\x03\x65xt\x12\r.SessionEvent\x18\xef\x07 \x01(\x0b\x32\x11.Event_UserJoined')
  ,
  dependencies=[session__event__pb2.DESCRIPTOR,serverinfo__user__pb2.DESCRIPTOR,])




_EVENT_USERJOINED = _descriptor.Descriptor(
  name='Event_UserJoined',
  full_name='Event_UserJoined',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_info', full_name='Event_UserJoined.user_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Event_UserJoined.ext', index=0,
      number=1007, type=11, cpp_type=10, label=1,
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
  serialized_end=174,
)

_EVENT_USERJOINED.fields_by_name['user_info'].message_type = serverinfo__user__pb2._SERVERINFO_USER
DESCRIPTOR.message_types_by_name['Event_UserJoined'] = _EVENT_USERJOINED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Event_UserJoined = _reflection.GeneratedProtocolMessageType('Event_UserJoined', (_message.Message,), dict(
  DESCRIPTOR = _EVENT_USERJOINED,
  __module__ = 'event_user_joined_pb2'
  # @@protoc_insertion_point(class_scope:Event_UserJoined)
  ))
_sym_db.RegisterMessage(Event_UserJoined)

_EVENT_USERJOINED.extensions_by_name['ext'].message_type = _EVENT_USERJOINED
session__event__pb2.SessionEvent.RegisterExtension(_EVENT_USERJOINED.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
