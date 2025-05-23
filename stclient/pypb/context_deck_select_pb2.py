# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: context_deck_select.proto

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
  name='context_deck_select.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x19\x63ontext_deck_select.proto\x1a\x18game_event_context.proto\"y\n\x12\x43ontext_DeckSelect\x12\x11\n\tdeck_hash\x18\x01 \x01(\t\x12\x1a\n\x0esideboard_size\x18\x02 \x01(\x05:\x02-124\n\x03\x65xt\x12\x11.GameEventContext\x18\xea\x07 \x01(\x0b\x32\x13.Context_DeckSelect')
  ,
  dependencies=[game__event__context__pb2.DESCRIPTOR,])




_CONTEXT_DECKSELECT = _descriptor.Descriptor(
  name='Context_DeckSelect',
  full_name='Context_DeckSelect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deck_hash', full_name='Context_DeckSelect.deck_hash', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sideboard_size', full_name='Context_DeckSelect.sideboard_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Context_DeckSelect.ext', index=0,
      number=1002, type=11, cpp_type=10, label=1,
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
  serialized_start=55,
  serialized_end=176,
)

DESCRIPTOR.message_types_by_name['Context_DeckSelect'] = _CONTEXT_DECKSELECT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Context_DeckSelect = _reflection.GeneratedProtocolMessageType('Context_DeckSelect', (_message.Message,), dict(
  DESCRIPTOR = _CONTEXT_DECKSELECT,
  __module__ = 'context_deck_select_pb2'
  # @@protoc_insertion_point(class_scope:Context_DeckSelect)
  ))
_sym_db.RegisterMessage(Context_DeckSelect)

_CONTEXT_DECKSELECT.extensions_by_name['ext'].message_type = _CONTEXT_DECKSELECT
game__event__context__pb2.GameEventContext.RegisterExtension(_CONTEXT_DECKSELECT.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
