# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: serverinfo_playerping.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='serverinfo_playerping.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1bserverinfo_playerping.proto\"=\n\x15ServerInfo_PlayerPing\x12\x11\n\tplayer_id\x18\x01 \x01(\x11\x12\x11\n\tping_time\x18\x02 \x01(\x11')
)




_SERVERINFO_PLAYERPING = _descriptor.Descriptor(
  name='ServerInfo_PlayerPing',
  full_name='ServerInfo_PlayerPing',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_id', full_name='ServerInfo_PlayerPing.player_id', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ping_time', full_name='ServerInfo_PlayerPing.ping_time', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
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
  serialized_start=31,
  serialized_end=92,
)

DESCRIPTOR.message_types_by_name['ServerInfo_PlayerPing'] = _SERVERINFO_PLAYERPING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServerInfo_PlayerPing = _reflection.GeneratedProtocolMessageType('ServerInfo_PlayerPing', (_message.Message,), dict(
  DESCRIPTOR = _SERVERINFO_PLAYERPING,
  __module__ = 'serverinfo_playerping_pb2'
  # @@protoc_insertion_point(class_scope:ServerInfo_PlayerPing)
  ))
_sym_db.RegisterMessage(ServerInfo_PlayerPing)


# @@protoc_insertion_point(module_scope)
