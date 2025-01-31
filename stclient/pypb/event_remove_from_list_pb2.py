# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event_remove_from_list.proto

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
  name='event_remove_from_list.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1c\x65vent_remove_from_list.proto\x1a\x13session_event.proto\"p\n\x14\x45vent_RemoveFromList\x12\x11\n\tlist_name\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t22\n\x03\x65xt\x12\r.SessionEvent\x18\xee\x07 \x01(\x0b\x32\x15.Event_RemoveFromList')
  ,
  dependencies=[session__event__pb2.DESCRIPTOR,])




_EVENT_REMOVEFROMLIST = _descriptor.Descriptor(
  name='Event_RemoveFromList',
  full_name='Event_RemoveFromList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='list_name', full_name='Event_RemoveFromList.list_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='Event_RemoveFromList.user_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Event_RemoveFromList.ext', index=0,
      number=1006, type=11, cpp_type=10, label=1,
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
  serialized_start=53,
  serialized_end=165,
)

DESCRIPTOR.message_types_by_name['Event_RemoveFromList'] = _EVENT_REMOVEFROMLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Event_RemoveFromList = _reflection.GeneratedProtocolMessageType('Event_RemoveFromList', (_message.Message,), dict(
  DESCRIPTOR = _EVENT_REMOVEFROMLIST,
  __module__ = 'event_remove_from_list_pb2'
  # @@protoc_insertion_point(class_scope:Event_RemoveFromList)
  ))
_sym_db.RegisterMessage(Event_RemoveFromList)

_EVENT_REMOVEFROMLIST.extensions_by_name['ext'].message_type = _EVENT_REMOVEFROMLIST
session__event__pb2.SessionEvent.RegisterExtension(_EVENT_REMOVEFROMLIST.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
