# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event_leave_room.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import room_event_pb2 as room__event__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='event_leave_room.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x16\x65vent_leave_room.proto\x1a\x10room_event.proto\"K\n\x0f\x45vent_LeaveRoom\x12\x0c\n\x04name\x18\x01 \x01(\t2*\n\x03\x65xt\x12\n.RoomEvent\x18\xe8\x07 \x01(\x0b\x32\x10.Event_LeaveRoom')
  ,
  dependencies=[room__event__pb2.DESCRIPTOR,])




_EVENT_LEAVEROOM = _descriptor.Descriptor(
  name='Event_LeaveRoom',
  full_name='Event_LeaveRoom',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Event_LeaveRoom.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Event_LeaveRoom.ext', index=0,
      number=1000, type=11, cpp_type=10, label=1,
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
  serialized_start=44,
  serialized_end=119,
)

DESCRIPTOR.message_types_by_name['Event_LeaveRoom'] = _EVENT_LEAVEROOM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Event_LeaveRoom = _reflection.GeneratedProtocolMessageType('Event_LeaveRoom', (_message.Message,), dict(
  DESCRIPTOR = _EVENT_LEAVEROOM,
  __module__ = 'event_leave_room_pb2'
  # @@protoc_insertion_point(class_scope:Event_LeaveRoom)
  ))
_sym_db.RegisterMessage(Event_LeaveRoom)

_EVENT_LEAVEROOM.extensions_by_name['ext'].message_type = _EVENT_LEAVEROOM
room__event__pb2.RoomEvent.RegisterExtension(_EVENT_LEAVEROOM.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
