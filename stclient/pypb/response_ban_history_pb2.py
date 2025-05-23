# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: response_ban_history.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import response_pb2 as response__pb2
from . import serverinfo_ban_pb2 as serverinfo__ban__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='response_ban_history.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1aresponse_ban_history.proto\x1a\x0eresponse.proto\x1a\x14serverinfo_ban.proto\"g\n\x13Response_BanHistory\x12!\n\x08\x62\x61n_list\x18\x01 \x03(\x0b\x32\x0f.ServerInfo_Ban2-\n\x03\x65xt\x12\t.Response\x18\xf4\x07 \x01(\x0b\x32\x14.Response_BanHistory')
  ,
  dependencies=[response__pb2.DESCRIPTOR,serverinfo__ban__pb2.DESCRIPTOR,])




_RESPONSE_BANHISTORY = _descriptor.Descriptor(
  name='Response_BanHistory',
  full_name='Response_BanHistory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ban_list', full_name='Response_BanHistory.ban_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Response_BanHistory.ext', index=0,
      number=1012, type=11, cpp_type=10, label=1,
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
  serialized_start=68,
  serialized_end=171,
)

_RESPONSE_BANHISTORY.fields_by_name['ban_list'].message_type = serverinfo__ban__pb2._SERVERINFO_BAN
DESCRIPTOR.message_types_by_name['Response_BanHistory'] = _RESPONSE_BANHISTORY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Response_BanHistory = _reflection.GeneratedProtocolMessageType('Response_BanHistory', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE_BANHISTORY,
  __module__ = 'response_ban_history_pb2'
  # @@protoc_insertion_point(class_scope:Response_BanHistory)
  ))
_sym_db.RegisterMessage(Response_BanHistory)

_RESPONSE_BANHISTORY.extensions_by_name['ext'].message_type = _RESPONSE_BANHISTORY
response__pb2.Response.RegisterExtension(_RESPONSE_BANHISTORY.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
