# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event_replay_added.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import session_event_pb2 as session__event__pb2
from . import serverinfo_replay_match_pb2 as serverinfo__replay__match__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='event_replay_added.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x18\x65vent_replay_added.proto\x1a\x13session_event.proto\x1a\x1dserverinfo_replay_match.proto\"q\n\x11\x45vent_ReplayAdded\x12+\n\nmatch_info\x18\x01 \x01(\x0b\x32\x17.ServerInfo_ReplayMatch2/\n\x03\x65xt\x12\r.SessionEvent\x18\xcc\x08 \x01(\x0b\x32\x12.Event_ReplayAdded')
  ,
  dependencies=[session__event__pb2.DESCRIPTOR,serverinfo__replay__match__pb2.DESCRIPTOR,])




_EVENT_REPLAYADDED = _descriptor.Descriptor(
  name='Event_ReplayAdded',
  full_name='Event_ReplayAdded',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='match_info', full_name='Event_ReplayAdded.match_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Event_ReplayAdded.ext', index=0,
      number=1100, type=11, cpp_type=10, label=1,
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
  serialized_start=80,
  serialized_end=193,
)

_EVENT_REPLAYADDED.fields_by_name['match_info'].message_type = serverinfo__replay__match__pb2._SERVERINFO_REPLAYMATCH
DESCRIPTOR.message_types_by_name['Event_ReplayAdded'] = _EVENT_REPLAYADDED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Event_ReplayAdded = _reflection.GeneratedProtocolMessageType('Event_ReplayAdded', (_message.Message,), dict(
  DESCRIPTOR = _EVENT_REPLAYADDED,
  __module__ = 'event_replay_added_pb2'
  # @@protoc_insertion_point(class_scope:Event_ReplayAdded)
  ))
_sym_db.RegisterMessage(Event_ReplayAdded)

_EVENT_REPLAYADDED.extensions_by_name['ext'].message_type = _EVENT_REPLAYADDED
session__event__pb2.SessionEvent.RegisterExtension(_EVENT_REPLAYADDED.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
