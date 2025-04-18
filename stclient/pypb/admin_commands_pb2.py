# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: admin_commands.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='admin_commands.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x14\x61\x64min_commands.proto\"\x83\x01\n\x0c\x41\x64minCommand\"i\n\x10\x41\x64minCommandType\x12\x1a\n\x15UPDATE_SERVER_MESSAGE\x10\xe8\x07\x12\x14\n\x0fSHUTDOWN_SERVER\x10\xe9\x07\x12\x12\n\rRELOAD_CONFIG\x10\xea\x07\x12\x0f\n\nADJUST_MOD\x10\xeb\x07*\x08\x08\x64\x10\x80\x80\x80\x80\x02\"X\n\x1b\x43ommand_UpdateServerMessage29\n\x03\x65xt\x12\r.AdminCommand\x18\xe8\x07 \x01(\x0b\x32\x1c.Command_UpdateServerMessage\"o\n\x16\x43ommand_ShutdownServer\x12\x0e\n\x06reason\x18\x01 \x01(\t\x12\x0f\n\x07minutes\x18\x02 \x01(\r24\n\x03\x65xt\x12\r.AdminCommand\x18\xe9\x07 \x01(\x0b\x32\x17.Command_ShutdownServer\"J\n\x14\x43ommand_ReloadConfig22\n\x03\x65xt\x12\r.AdminCommand\x18\xea\x07 \x01(\x0b\x32\x15.Command_ReloadConfig\"\x87\x01\n\x11\x43ommand_AdjustMod\x12\x11\n\tuser_name\x18\x01 \x02(\t\x12\x15\n\rshould_be_mod\x18\x02 \x01(\x08\x12\x17\n\x0fshould_be_judge\x18\x03 \x01(\x08\x32/\n\x03\x65xt\x12\r.AdminCommand\x18\xeb\x07 \x01(\x0b\x32\x12.Command_AdjustMod')
)



_ADMINCOMMAND_ADMINCOMMANDTYPE = _descriptor.EnumDescriptor(
  name='AdminCommandType',
  full_name='AdminCommand.AdminCommandType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UPDATE_SERVER_MESSAGE', index=0, number=1000,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHUTDOWN_SERVER', index=1, number=1001,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RELOAD_CONFIG', index=2, number=1002,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADJUST_MOD', index=3, number=1003,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=41,
  serialized_end=146,
)
_sym_db.RegisterEnumDescriptor(_ADMINCOMMAND_ADMINCOMMANDTYPE)


_ADMINCOMMAND = _descriptor.Descriptor(
  name='AdminCommand',
  full_name='AdminCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ADMINCOMMAND_ADMINCOMMANDTYPE,
  ],
  serialized_options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(100, 536870912), ],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=156,
)


_COMMAND_UPDATESERVERMESSAGE = _descriptor.Descriptor(
  name='Command_UpdateServerMessage',
  full_name='Command_UpdateServerMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Command_UpdateServerMessage.ext', index=0,
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
  serialized_start=158,
  serialized_end=246,
)


_COMMAND_SHUTDOWNSERVER = _descriptor.Descriptor(
  name='Command_ShutdownServer',
  full_name='Command_ShutdownServer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reason', full_name='Command_ShutdownServer.reason', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minutes', full_name='Command_ShutdownServer.minutes', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Command_ShutdownServer.ext', index=0,
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
  serialized_start=248,
  serialized_end=359,
)


_COMMAND_RELOADCONFIG = _descriptor.Descriptor(
  name='Command_ReloadConfig',
  full_name='Command_ReloadConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Command_ReloadConfig.ext', index=0,
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
  serialized_start=361,
  serialized_end=435,
)


_COMMAND_ADJUSTMOD = _descriptor.Descriptor(
  name='Command_AdjustMod',
  full_name='Command_AdjustMod',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_name', full_name='Command_AdjustMod.user_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='should_be_mod', full_name='Command_AdjustMod.should_be_mod', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='should_be_judge', full_name='Command_AdjustMod.should_be_judge', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Command_AdjustMod.ext', index=0,
      number=1003, type=11, cpp_type=10, label=1,
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
  serialized_start=438,
  serialized_end=573,
)

_ADMINCOMMAND_ADMINCOMMANDTYPE.containing_type = _ADMINCOMMAND
DESCRIPTOR.message_types_by_name['AdminCommand'] = _ADMINCOMMAND
DESCRIPTOR.message_types_by_name['Command_UpdateServerMessage'] = _COMMAND_UPDATESERVERMESSAGE
DESCRIPTOR.message_types_by_name['Command_ShutdownServer'] = _COMMAND_SHUTDOWNSERVER
DESCRIPTOR.message_types_by_name['Command_ReloadConfig'] = _COMMAND_RELOADCONFIG
DESCRIPTOR.message_types_by_name['Command_AdjustMod'] = _COMMAND_ADJUSTMOD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdminCommand = _reflection.GeneratedProtocolMessageType('AdminCommand', (_message.Message,), dict(
  DESCRIPTOR = _ADMINCOMMAND,
  __module__ = 'admin_commands_pb2'
  # @@protoc_insertion_point(class_scope:AdminCommand)
  ))
_sym_db.RegisterMessage(AdminCommand)

Command_UpdateServerMessage = _reflection.GeneratedProtocolMessageType('Command_UpdateServerMessage', (_message.Message,), dict(
  DESCRIPTOR = _COMMAND_UPDATESERVERMESSAGE,
  __module__ = 'admin_commands_pb2'
  # @@protoc_insertion_point(class_scope:Command_UpdateServerMessage)
  ))
_sym_db.RegisterMessage(Command_UpdateServerMessage)

Command_ShutdownServer = _reflection.GeneratedProtocolMessageType('Command_ShutdownServer', (_message.Message,), dict(
  DESCRIPTOR = _COMMAND_SHUTDOWNSERVER,
  __module__ = 'admin_commands_pb2'
  # @@protoc_insertion_point(class_scope:Command_ShutdownServer)
  ))
_sym_db.RegisterMessage(Command_ShutdownServer)

Command_ReloadConfig = _reflection.GeneratedProtocolMessageType('Command_ReloadConfig', (_message.Message,), dict(
  DESCRIPTOR = _COMMAND_RELOADCONFIG,
  __module__ = 'admin_commands_pb2'
  # @@protoc_insertion_point(class_scope:Command_ReloadConfig)
  ))
_sym_db.RegisterMessage(Command_ReloadConfig)

Command_AdjustMod = _reflection.GeneratedProtocolMessageType('Command_AdjustMod', (_message.Message,), dict(
  DESCRIPTOR = _COMMAND_ADJUSTMOD,
  __module__ = 'admin_commands_pb2'
  # @@protoc_insertion_point(class_scope:Command_AdjustMod)
  ))
_sym_db.RegisterMessage(Command_AdjustMod)

_COMMAND_UPDATESERVERMESSAGE.extensions_by_name['ext'].message_type = _COMMAND_UPDATESERVERMESSAGE
AdminCommand.RegisterExtension(_COMMAND_UPDATESERVERMESSAGE.extensions_by_name['ext'])
_COMMAND_SHUTDOWNSERVER.extensions_by_name['ext'].message_type = _COMMAND_SHUTDOWNSERVER
AdminCommand.RegisterExtension(_COMMAND_SHUTDOWNSERVER.extensions_by_name['ext'])
_COMMAND_RELOADCONFIG.extensions_by_name['ext'].message_type = _COMMAND_RELOADCONFIG
AdminCommand.RegisterExtension(_COMMAND_RELOADCONFIG.extensions_by_name['ext'])
_COMMAND_ADJUSTMOD.extensions_by_name['ext'].message_type = _COMMAND_ADJUSTMOD
AdminCommand.RegisterExtension(_COMMAND_ADJUSTMOD.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
