# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import response_pb2 as response__pb2
from . import session_event_pb2 as session__event__pb2
from . import game_event_container_pb2 as game__event__container__pb2
from . import room_event_pb2 as room__event__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='server_message.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x14server_message.proto\x1a\x0eresponse.proto\x1a\x13session_event.proto\x1a\x1agame_event_container.proto\x1a\x10room_event.proto\"\xb1\x02\n\rServerMessage\x12\x30\n\x0cmessage_type\x18\x01 \x01(\x0e\x32\x1a.ServerMessage.MessageType\x12\x1b\n\x08response\x18\x02 \x01(\x0b\x32\t.Response\x12$\n\rsession_event\x18\x03 \x01(\x0b\x32\r.SessionEvent\x12\x31\n\x14game_event_container\x18\x04 \x01(\x0b\x32\x13.GameEventContainer\x12\x1e\n\nroom_event\x18\x05 \x01(\x0b\x32\n.RoomEvent\"X\n\x0bMessageType\x12\x0c\n\x08RESPONSE\x10\x00\x12\x11\n\rSESSION_EVENT\x10\x01\x12\x18\n\x14GAME_EVENT_CONTAINER\x10\x02\x12\x0e\n\nROOM_EVENT\x10\x03')
  ,
  dependencies=[response__pb2.DESCRIPTOR,session__event__pb2.DESCRIPTOR,game__event__container__pb2.DESCRIPTOR,room__event__pb2.DESCRIPTOR,])



_SERVERMESSAGE_MESSAGETYPE = _descriptor.EnumDescriptor(
  name='MessageType',
  full_name='ServerMessage.MessageType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RESPONSE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SESSION_EVENT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAME_EVENT_CONTAINER', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROOM_EVENT', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=325,
  serialized_end=413,
)
_sym_db.RegisterEnumDescriptor(_SERVERMESSAGE_MESSAGETYPE)


_SERVERMESSAGE = _descriptor.Descriptor(
  name='ServerMessage',
  full_name='ServerMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_type', full_name='ServerMessage.message_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response', full_name='ServerMessage.response', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='session_event', full_name='ServerMessage.session_event', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='game_event_container', full_name='ServerMessage.game_event_container', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='room_event', full_name='ServerMessage.room_event', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SERVERMESSAGE_MESSAGETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=108,
  serialized_end=413,
)

_SERVERMESSAGE.fields_by_name['message_type'].enum_type = _SERVERMESSAGE_MESSAGETYPE
_SERVERMESSAGE.fields_by_name['response'].message_type = response__pb2._RESPONSE
_SERVERMESSAGE.fields_by_name['session_event'].message_type = session__event__pb2._SESSIONEVENT
_SERVERMESSAGE.fields_by_name['game_event_container'].message_type = game__event__container__pb2._GAMEEVENTCONTAINER
_SERVERMESSAGE.fields_by_name['room_event'].message_type = room__event__pb2._ROOMEVENT
_SERVERMESSAGE_MESSAGETYPE.containing_type = _SERVERMESSAGE
DESCRIPTOR.message_types_by_name['ServerMessage'] = _SERVERMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServerMessage = _reflection.GeneratedProtocolMessageType('ServerMessage', (_message.Message,), dict(
  DESCRIPTOR = _SERVERMESSAGE,
  __module__ = 'server_message_pb2'
  # @@protoc_insertion_point(class_scope:ServerMessage)
  ))
_sym_db.RegisterMessage(ServerMessage)


# @@protoc_insertion_point(module_scope)
