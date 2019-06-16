# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: serverinfo_player.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import serverinfo_zone_pb2 as serverinfo__zone__pb2
from . import serverinfo_counter_pb2 as serverinfo__counter__pb2
from . import serverinfo_arrow_pb2 as serverinfo__arrow__pb2
from . import serverinfo_playerproperties_pb2 as serverinfo__playerproperties__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='serverinfo_player.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x17serverinfo_player.proto\x1a\x15serverinfo_zone.proto\x1a\x18serverinfo_counter.proto\x1a\x16serverinfo_arrow.proto\x1a!serverinfo_playerproperties.proto\"\xcf\x01\n\x11ServerInfo_Player\x12\x30\n\nproperties\x18\x01 \x01(\x0b\x32\x1c.ServerInfo_PlayerProperties\x12\x11\n\tdeck_list\x18\x02 \x01(\t\x12#\n\tzone_list\x18\x03 \x03(\x0b\x32\x10.ServerInfo_Zone\x12)\n\x0c\x63ounter_list\x18\x04 \x03(\x0b\x32\x13.ServerInfo_Counter\x12%\n\narrow_list\x18\x05 \x03(\x0b\x32\x11.ServerInfo_Arrow')
  ,
  dependencies=[serverinfo__zone__pb2.DESCRIPTOR,serverinfo__counter__pb2.DESCRIPTOR,serverinfo__arrow__pb2.DESCRIPTOR,serverinfo__playerproperties__pb2.DESCRIPTOR,])




_SERVERINFO_PLAYER = _descriptor.Descriptor(
  name='ServerInfo_Player',
  full_name='ServerInfo_Player',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='properties', full_name='ServerInfo_Player.properties', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deck_list', full_name='ServerInfo_Player.deck_list', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zone_list', full_name='ServerInfo_Player.zone_list', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='counter_list', full_name='ServerInfo_Player.counter_list', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='arrow_list', full_name='ServerInfo_Player.arrow_list', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=136,
  serialized_end=343,
)

_SERVERINFO_PLAYER.fields_by_name['properties'].message_type = serverinfo__playerproperties__pb2._SERVERINFO_PLAYERPROPERTIES
_SERVERINFO_PLAYER.fields_by_name['zone_list'].message_type = serverinfo__zone__pb2._SERVERINFO_ZONE
_SERVERINFO_PLAYER.fields_by_name['counter_list'].message_type = serverinfo__counter__pb2._SERVERINFO_COUNTER
_SERVERINFO_PLAYER.fields_by_name['arrow_list'].message_type = serverinfo__arrow__pb2._SERVERINFO_ARROW
DESCRIPTOR.message_types_by_name['ServerInfo_Player'] = _SERVERINFO_PLAYER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServerInfo_Player = _reflection.GeneratedProtocolMessageType('ServerInfo_Player', (_message.Message,), dict(
  DESCRIPTOR = _SERVERINFO_PLAYER,
  __module__ = 'serverinfo_player_pb2'
  # @@protoc_insertion_point(class_scope:ServerInfo_Player)
  ))
_sym_db.RegisterMessage(ServerInfo_Player)


# @@protoc_insertion_point(module_scope)
