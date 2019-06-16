# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: response_deck_list.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import response_pb2 as response__pb2
from . import serverinfo_deckstorage_pb2 as serverinfo__deckstorage__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='response_deck_list.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x18response_deck_list.proto\x1a\x0eresponse.proto\x1a\x1cserverinfo_deckstorage.proto\"n\n\x11Response_DeckList\x12,\n\x04root\x18\x01 \x01(\x0b\x32\x1e.ServerInfo_DeckStorage_Folder2+\n\x03\x65xt\x12\t.Response\x18\xee\x07 \x01(\x0b\x32\x12.Response_DeckList')
  ,
  dependencies=[response__pb2.DESCRIPTOR,serverinfo__deckstorage__pb2.DESCRIPTOR,])




_RESPONSE_DECKLIST = _descriptor.Descriptor(
  name='Response_DeckList',
  full_name='Response_DeckList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='root', full_name='Response_DeckList.root', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Response_DeckList.ext', index=0,
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
  serialized_start=74,
  serialized_end=184,
)

_RESPONSE_DECKLIST.fields_by_name['root'].message_type = serverinfo__deckstorage__pb2._SERVERINFO_DECKSTORAGE_FOLDER
DESCRIPTOR.message_types_by_name['Response_DeckList'] = _RESPONSE_DECKLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Response_DeckList = _reflection.GeneratedProtocolMessageType('Response_DeckList', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE_DECKLIST,
  __module__ = 'response_deck_list_pb2'
  # @@protoc_insertion_point(class_scope:Response_DeckList)
  ))
_sym_db.RegisterMessage(Response_DeckList)

_RESPONSE_DECKLIST.extensions_by_name['ext'].message_type = _RESPONSE_DECKLIST
response__pb2.Response.RegisterExtension(_RESPONSE_DECKLIST.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
