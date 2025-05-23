# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: response_register.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import response_pb2 as response__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='response_register.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x17response_register.proto\x1a\x0eresponse.proto\"t\n\x11Response_Register\x12\x19\n\x11\x64\x65nied_reason_str\x18\x01 \x01(\t\x12\x17\n\x0f\x64\x65nied_end_time\x18\x02 \x01(\x04\x32+\n\x03\x65xt\x12\t.Response\x18\xf1\x07 \x01(\x0b\x32\x12.Response_Register')
  ,
  dependencies=[response__pb2.DESCRIPTOR,])




_RESPONSE_REGISTER = _descriptor.Descriptor(
  name='Response_Register',
  full_name='Response_Register',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='denied_reason_str', full_name='Response_Register.denied_reason_str', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='denied_end_time', full_name='Response_Register.denied_end_time', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Response_Register.ext', index=0,
      number=1009, type=11, cpp_type=10, label=1,
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
  serialized_start=43,
  serialized_end=159,
)

DESCRIPTOR.message_types_by_name['Response_Register'] = _RESPONSE_REGISTER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Response_Register = _reflection.GeneratedProtocolMessageType('Response_Register', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE_REGISTER,
  __module__ = 'response_register_pb2'
  # @@protoc_insertion_point(class_scope:Response_Register)
  ))
_sym_db.RegisterMessage(Response_Register)

_RESPONSE_REGISTER.extensions_by_name['ext'].message_type = _RESPONSE_REGISTER
response__pb2.Response.RegisterExtension(_RESPONSE_REGISTER.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
