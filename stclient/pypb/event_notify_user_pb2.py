# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event_notify_user.proto

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
  name='event_notify_user.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x17\x65vent_notify_user.proto\x1a\x13session_event.proto\"\x93\x02\n\x10\x45vent_NotifyUser\x12\x30\n\x04type\x18\x01 \x01(\x0e\x32\".Event_NotifyUser.NotificationType\x12\x16\n\x0ewarning_reason\x18\x02 \x01(\t\x12\x14\n\x0c\x63ustom_title\x18\x03 \x01(\t\x12\x16\n\x0e\x63ustom_content\x18\x04 \x01(\t\"W\n\x10NotificationType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08PROMOTED\x10\x01\x12\x0b\n\x07WARNING\x10\x02\x12\x0f\n\x0bIDLEWARNING\x10\x03\x12\n\n\x06\x43USTOM\x10\x04\x32.\n\x03\x65xt\x12\r.SessionEvent\x18\xf2\x07 \x01(\x0b\x32\x11.Event_NotifyUser')
  ,
  dependencies=[session__event__pb2.DESCRIPTOR,])



_EVENT_NOTIFYUSER_NOTIFICATIONTYPE = _descriptor.EnumDescriptor(
  name='NotificationType',
  full_name='Event_NotifyUser.NotificationType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROMOTED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WARNING', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IDLEWARNING', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=189,
  serialized_end=276,
)
_sym_db.RegisterEnumDescriptor(_EVENT_NOTIFYUSER_NOTIFICATIONTYPE)


_EVENT_NOTIFYUSER = _descriptor.Descriptor(
  name='Event_NotifyUser',
  full_name='Event_NotifyUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Event_NotifyUser.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='warning_reason', full_name='Event_NotifyUser.warning_reason', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='custom_title', full_name='Event_NotifyUser.custom_title', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='custom_content', full_name='Event_NotifyUser.custom_content', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Event_NotifyUser.ext', index=0,
      number=1010, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  nested_types=[],
  enum_types=[
    _EVENT_NOTIFYUSER_NOTIFICATIONTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=324,
)

_EVENT_NOTIFYUSER.fields_by_name['type'].enum_type = _EVENT_NOTIFYUSER_NOTIFICATIONTYPE
_EVENT_NOTIFYUSER_NOTIFICATIONTYPE.containing_type = _EVENT_NOTIFYUSER
DESCRIPTOR.message_types_by_name['Event_NotifyUser'] = _EVENT_NOTIFYUSER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Event_NotifyUser = _reflection.GeneratedProtocolMessageType('Event_NotifyUser', (_message.Message,), dict(
  DESCRIPTOR = _EVENT_NOTIFYUSER,
  __module__ = 'event_notify_user_pb2'
  # @@protoc_insertion_point(class_scope:Event_NotifyUser)
  ))
_sym_db.RegisterMessage(Event_NotifyUser)

_EVENT_NOTIFYUSER.extensions_by_name['ext'].message_type = _EVENT_NOTIFYUSER
session__event__pb2.SessionEvent.RegisterExtension(_EVENT_NOTIFYUSER.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
