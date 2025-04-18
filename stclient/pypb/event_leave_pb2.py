# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event_leave.proto

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
  name='event_leave.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x11\x65vent_leave.proto\x1a\x10game_event.proto\"\xb0\x01\n\x0b\x45vent_Leave\x12(\n\x06reason\x18\x01 \x01(\x0e\x32\x18.Event_Leave.LeaveReason\"O\n\x0bLeaveReason\x12\t\n\x05OTHER\x10\x01\x12\x0f\n\x0bUSER_KICKED\x10\x02\x12\r\n\tUSER_LEFT\x10\x03\x12\x15\n\x11USER_DISCONNECTED\x10\x04\x32&\n\x03\x65xt\x12\n.GameEvent\x18\xe9\x07 \x01(\x0b\x32\x0c.Event_Leave')
  ,
  dependencies=[game__event__pb2.DESCRIPTOR,])



_EVENT_LEAVE_LEAVEREASON = _descriptor.EnumDescriptor(
  name='LeaveReason',
  full_name='Event_Leave.LeaveReason',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OTHER', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USER_KICKED', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USER_LEFT', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USER_DISCONNECTED', index=3, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=97,
  serialized_end=176,
)
_sym_db.RegisterEnumDescriptor(_EVENT_LEAVE_LEAVEREASON)


_EVENT_LEAVE = _descriptor.Descriptor(
  name='Event_Leave',
  full_name='Event_Leave',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reason', full_name='Event_Leave.reason', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Event_Leave.ext', index=0,
      number=1001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  nested_types=[],
  enum_types=[
    _EVENT_LEAVE_LEAVEREASON,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=216,
)

_EVENT_LEAVE.fields_by_name['reason'].enum_type = _EVENT_LEAVE_LEAVEREASON
_EVENT_LEAVE_LEAVEREASON.containing_type = _EVENT_LEAVE
DESCRIPTOR.message_types_by_name['Event_Leave'] = _EVENT_LEAVE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Event_Leave = _reflection.GeneratedProtocolMessageType('Event_Leave', (_message.Message,), dict(
  DESCRIPTOR = _EVENT_LEAVE,
  __module__ = 'event_leave_pb2'
  # @@protoc_insertion_point(class_scope:Event_Leave)
  ))
_sym_db.RegisterMessage(Event_Leave)

_EVENT_LEAVE.extensions_by_name['ext'].message_type = _EVENT_LEAVE
game__event__pb2.GameEvent.RegisterExtension(_EVENT_LEAVE.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
