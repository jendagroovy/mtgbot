# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: response_join_room.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import response_pb2 as response__pb2
from . import serverinfo_room_pb2 as serverinfo__room__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='response_join_room.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x18response_join_room.proto\x1a\x0eresponse.proto\x1a\x15serverinfo_room.proto\"e\n\x11Response_JoinRoom\x12#\n\troom_info\x18\x01 \x01(\x0b\x32\x10.ServerInfo_Room2+\n\x03\x65xt\x12\t.Response\x18\xe8\x07 \x01(\x0b\x32\x12.Response_JoinRoom')
  ,
  dependencies=[response__pb2.DESCRIPTOR,serverinfo__room__pb2.DESCRIPTOR,])




_RESPONSE_JOINROOM = _descriptor.Descriptor(
  name='Response_JoinRoom',
  full_name='Response_JoinRoom',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='room_info', full_name='Response_JoinRoom.room_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Response_JoinRoom.ext', index=0,
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
  serialized_start=67,
  serialized_end=168,
)

_RESPONSE_JOINROOM.fields_by_name['room_info'].message_type = serverinfo__room__pb2._SERVERINFO_ROOM
DESCRIPTOR.message_types_by_name['Response_JoinRoom'] = _RESPONSE_JOINROOM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Response_JoinRoom = _reflection.GeneratedProtocolMessageType('Response_JoinRoom', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE_JOINROOM,
  __module__ = 'response_join_room_pb2'
  # @@protoc_insertion_point(class_scope:Response_JoinRoom)
  ))
_sym_db.RegisterMessage(Response_JoinRoom)

_RESPONSE_JOINROOM.extensions_by_name['ext'].message_type = _RESPONSE_JOINROOM
response__pb2.Response.RegisterExtension(_RESPONSE_JOINROOM.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
