# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: context_concede.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import game_event_context_pb2 as game__event__context__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='context_concede.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x15\x63ontext_concede.proto\x1a\x18game_event_context.proto\"D\n\x0f\x43ontext_Concede21\n\x03\x65xt\x12\x11.GameEventContext\x18\xe9\x07 \x01(\x0b\x32\x10.Context_Concede\"H\n\x11\x43ontext_Unconcede23\n\x03\x65xt\x12\x11.GameEventContext\x18\xf1\x07 \x01(\x0b\x32\x12.Context_Unconcede')
  ,
  dependencies=[game__event__context__pb2.DESCRIPTOR,])




_CONTEXT_CONCEDE = _descriptor.Descriptor(
  name='Context_Concede',
  full_name='Context_Concede',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Context_Concede.ext', index=0,
      number=1001, type=11, cpp_type=10, label=1,
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
  serialized_start=51,
  serialized_end=119,
)


_CONTEXT_UNCONCEDE = _descriptor.Descriptor(
  name='Context_Unconcede',
  full_name='Context_Unconcede',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Context_Unconcede.ext', index=0,
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
  serialized_start=121,
  serialized_end=193,
)

DESCRIPTOR.message_types_by_name['Context_Concede'] = _CONTEXT_CONCEDE
DESCRIPTOR.message_types_by_name['Context_Unconcede'] = _CONTEXT_UNCONCEDE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Context_Concede = _reflection.GeneratedProtocolMessageType('Context_Concede', (_message.Message,), dict(
  DESCRIPTOR = _CONTEXT_CONCEDE,
  __module__ = 'context_concede_pb2'
  # @@protoc_insertion_point(class_scope:Context_Concede)
  ))
_sym_db.RegisterMessage(Context_Concede)

Context_Unconcede = _reflection.GeneratedProtocolMessageType('Context_Unconcede', (_message.Message,), dict(
  DESCRIPTOR = _CONTEXT_UNCONCEDE,
  __module__ = 'context_concede_pb2'
  # @@protoc_insertion_point(class_scope:Context_Unconcede)
  ))
_sym_db.RegisterMessage(Context_Unconcede)

_CONTEXT_CONCEDE.extensions_by_name['ext'].message_type = _CONTEXT_CONCEDE
game__event__context__pb2.GameEventContext.RegisterExtension(_CONTEXT_CONCEDE.extensions_by_name['ext'])
_CONTEXT_UNCONCEDE.extensions_by_name['ext'].message_type = _CONTEXT_UNCONCEDE
game__event__context__pb2.GameEventContext.RegisterExtension(_CONTEXT_UNCONCEDE.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
