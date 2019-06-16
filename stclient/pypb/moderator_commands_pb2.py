# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: moderator_commands.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='moderator_commands.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x18moderator_commands.proto\"\xa6\x01\n\x10ModeratorCommand\"\x87\x01\n\x14ModeratorCommandType\x12\x14\n\x0f\x42\x41N_FROM_SERVER\x10\xe8\x07\x12\x10\n\x0b\x42\x41N_HISTORY\x10\xe9\x07\x12\x0e\n\tWARN_USER\x10\xea\x07\x12\x11\n\x0cWARN_HISTORY\x10\xeb\x07\x12\x0e\n\tWARN_LIST\x10\xec\x07\x12\x14\n\x0fVIEWLOG_HISTORY\x10\xed\x07*\x08\x08\x64\x10\x80\x80\x80\x80\x02\"\xbf\x01\n\x15\x43ommand_BanFromServer\x12\x11\n\tuser_name\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x0f\n\x07minutes\x18\x03 \x01(\r\x12\x0e\n\x06reason\x18\x04 \x01(\t\x12\x16\n\x0evisible_reason\x18\x05 \x01(\t\x12\x10\n\x08\x63lientid\x18\x06 \x01(\t27\n\x03\x65xt\x12\x11.ModeratorCommand\x18\xe8\x07 \x01(\x0b\x32\x16.Command_BanFromServer\"c\n\x15\x43ommand_GetBanHistory\x12\x11\n\tuser_name\x18\x01 \x01(\t27\n\x03\x65xt\x12\x11.ModeratorCommand\x18\xe9\x07 \x01(\x0b\x32\x16.Command_GetBanHistory\"{\n\x10\x43ommand_WarnUser\x12\x11\n\tuser_name\x18\x01 \x01(\t\x12\x0e\n\x06reason\x18\x02 \x01(\t\x12\x10\n\x08\x63lientid\x18\x03 \x01(\t22\n\x03\x65xt\x12\x11.ModeratorCommand\x18\xea\x07 \x01(\x0b\x32\x11.Command_WarnUser\"e\n\x16\x43ommand_GetWarnHistory\x12\x11\n\tuser_name\x18\x01 \x01(\t28\n\x03\x65xt\x12\x11.ModeratorCommand\x18\xeb\x07 \x01(\x0b\x32\x17.Command_GetWarnHistory\"\x88\x01\n\x13\x43ommand_GetWarnList\x12\x10\n\x08mod_name\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t\x12\x15\n\ruser_clientid\x18\x03 \x01(\t25\n\x03\x65xt\x12\x11.ModeratorCommand\x18\xec\x07 \x01(\x0b\x32\x14.Command_GetWarnList\"\xf1\x01\n\x16\x43ommand_ViewLogHistory\x12\x11\n\tuser_name\x18\x01 \x01(\t\x12\x12\n\nip_address\x18\x02 \x01(\t\x12\x11\n\tgame_name\x18\x03 \x01(\t\x12\x0f\n\x07game_id\x18\x04 \x01(\t\x12\x0f\n\x07message\x18\x05 \x01(\t\x12\x14\n\x0clog_location\x18\x06 \x03(\t\x12\x12\n\ndate_range\x18\x07 \x02(\r\x12\x17\n\x0fmaximum_results\x18\x08 \x01(\r28\n\x03\x65xt\x12\x11.ModeratorCommand\x18\xed\x07 \x01(\x0b\x32\x17.Command_ViewLogHistory')
)



_MODERATORCOMMAND_MODERATORCOMMANDTYPE = _descriptor.EnumDescriptor(
  name='ModeratorCommandType',
  full_name='ModeratorCommand.ModeratorCommandType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BAN_FROM_SERVER', index=0, number=1000,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAN_HISTORY', index=1, number=1001,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WARN_USER', index=2, number=1002,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WARN_HISTORY', index=3, number=1003,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WARN_LIST', index=4, number=1004,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIEWLOG_HISTORY', index=5, number=1005,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=50,
  serialized_end=185,
)
_sym_db.RegisterEnumDescriptor(_MODERATORCOMMAND_MODERATORCOMMANDTYPE)


_MODERATORCOMMAND = _descriptor.Descriptor(
  name='ModeratorCommand',
  full_name='ModeratorCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MODERATORCOMMAND_MODERATORCOMMANDTYPE,
  ],
  serialized_options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(100, 536870912), ],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=195,
)


_COMMAND_BANFROMSERVER = _descriptor.Descriptor(
  name='Command_BanFromServer',
  full_name='Command_BanFromServer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_name', full_name='Command_BanFromServer.user_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='Command_BanFromServer.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minutes', full_name='Command_BanFromServer.minutes', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reason', full_name='Command_BanFromServer.reason', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='visible_reason', full_name='Command_BanFromServer.visible_reason', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clientid', full_name='Command_BanFromServer.clientid', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Command_BanFromServer.ext', index=0,
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
  serialized_start=198,
  serialized_end=389,
)


_COMMAND_GETBANHISTORY = _descriptor.Descriptor(
  name='Command_GetBanHistory',
  full_name='Command_GetBanHistory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_name', full_name='Command_GetBanHistory.user_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Command_GetBanHistory.ext', index=0,
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
  serialized_start=391,
  serialized_end=490,
)


_COMMAND_WARNUSER = _descriptor.Descriptor(
  name='Command_WarnUser',
  full_name='Command_WarnUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_name', full_name='Command_WarnUser.user_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reason', full_name='Command_WarnUser.reason', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clientid', full_name='Command_WarnUser.clientid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Command_WarnUser.ext', index=0,
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
  serialized_start=492,
  serialized_end=615,
)


_COMMAND_GETWARNHISTORY = _descriptor.Descriptor(
  name='Command_GetWarnHistory',
  full_name='Command_GetWarnHistory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_name', full_name='Command_GetWarnHistory.user_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Command_GetWarnHistory.ext', index=0,
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
  serialized_start=617,
  serialized_end=718,
)


_COMMAND_GETWARNLIST = _descriptor.Descriptor(
  name='Command_GetWarnList',
  full_name='Command_GetWarnList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mod_name', full_name='Command_GetWarnList.mod_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='Command_GetWarnList.user_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_clientid', full_name='Command_GetWarnList.user_clientid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Command_GetWarnList.ext', index=0,
      number=1004, type=11, cpp_type=10, label=1,
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
  serialized_start=721,
  serialized_end=857,
)


_COMMAND_VIEWLOGHISTORY = _descriptor.Descriptor(
  name='Command_ViewLogHistory',
  full_name='Command_ViewLogHistory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_name', full_name='Command_ViewLogHistory.user_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip_address', full_name='Command_ViewLogHistory.ip_address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='game_name', full_name='Command_ViewLogHistory.game_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='game_id', full_name='Command_ViewLogHistory.game_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='Command_ViewLogHistory.message', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log_location', full_name='Command_ViewLogHistory.log_location', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date_range', full_name='Command_ViewLogHistory.date_range', index=6,
      number=7, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maximum_results', full_name='Command_ViewLogHistory.maximum_results', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='Command_ViewLogHistory.ext', index=0,
      number=1005, type=11, cpp_type=10, label=1,
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
  serialized_start=860,
  serialized_end=1101,
)

_MODERATORCOMMAND_MODERATORCOMMANDTYPE.containing_type = _MODERATORCOMMAND
DESCRIPTOR.message_types_by_name['ModeratorCommand'] = _MODERATORCOMMAND
DESCRIPTOR.message_types_by_name['Command_BanFromServer'] = _COMMAND_BANFROMSERVER
DESCRIPTOR.message_types_by_name['Command_GetBanHistory'] = _COMMAND_GETBANHISTORY
DESCRIPTOR.message_types_by_name['Command_WarnUser'] = _COMMAND_WARNUSER
DESCRIPTOR.message_types_by_name['Command_GetWarnHistory'] = _COMMAND_GETWARNHISTORY
DESCRIPTOR.message_types_by_name['Command_GetWarnList'] = _COMMAND_GETWARNLIST
DESCRIPTOR.message_types_by_name['Command_ViewLogHistory'] = _COMMAND_VIEWLOGHISTORY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ModeratorCommand = _reflection.GeneratedProtocolMessageType('ModeratorCommand', (_message.Message,), dict(
  DESCRIPTOR = _MODERATORCOMMAND,
  __module__ = 'moderator_commands_pb2'
  # @@protoc_insertion_point(class_scope:ModeratorCommand)
  ))
_sym_db.RegisterMessage(ModeratorCommand)

Command_BanFromServer = _reflection.GeneratedProtocolMessageType('Command_BanFromServer', (_message.Message,), dict(
  DESCRIPTOR = _COMMAND_BANFROMSERVER,
  __module__ = 'moderator_commands_pb2'
  # @@protoc_insertion_point(class_scope:Command_BanFromServer)
  ))
_sym_db.RegisterMessage(Command_BanFromServer)

Command_GetBanHistory = _reflection.GeneratedProtocolMessageType('Command_GetBanHistory', (_message.Message,), dict(
  DESCRIPTOR = _COMMAND_GETBANHISTORY,
  __module__ = 'moderator_commands_pb2'
  # @@protoc_insertion_point(class_scope:Command_GetBanHistory)
  ))
_sym_db.RegisterMessage(Command_GetBanHistory)

Command_WarnUser = _reflection.GeneratedProtocolMessageType('Command_WarnUser', (_message.Message,), dict(
  DESCRIPTOR = _COMMAND_WARNUSER,
  __module__ = 'moderator_commands_pb2'
  # @@protoc_insertion_point(class_scope:Command_WarnUser)
  ))
_sym_db.RegisterMessage(Command_WarnUser)

Command_GetWarnHistory = _reflection.GeneratedProtocolMessageType('Command_GetWarnHistory', (_message.Message,), dict(
  DESCRIPTOR = _COMMAND_GETWARNHISTORY,
  __module__ = 'moderator_commands_pb2'
  # @@protoc_insertion_point(class_scope:Command_GetWarnHistory)
  ))
_sym_db.RegisterMessage(Command_GetWarnHistory)

Command_GetWarnList = _reflection.GeneratedProtocolMessageType('Command_GetWarnList', (_message.Message,), dict(
  DESCRIPTOR = _COMMAND_GETWARNLIST,
  __module__ = 'moderator_commands_pb2'
  # @@protoc_insertion_point(class_scope:Command_GetWarnList)
  ))
_sym_db.RegisterMessage(Command_GetWarnList)

Command_ViewLogHistory = _reflection.GeneratedProtocolMessageType('Command_ViewLogHistory', (_message.Message,), dict(
  DESCRIPTOR = _COMMAND_VIEWLOGHISTORY,
  __module__ = 'moderator_commands_pb2'
  # @@protoc_insertion_point(class_scope:Command_ViewLogHistory)
  ))
_sym_db.RegisterMessage(Command_ViewLogHistory)

_COMMAND_BANFROMSERVER.extensions_by_name['ext'].message_type = _COMMAND_BANFROMSERVER
ModeratorCommand.RegisterExtension(_COMMAND_BANFROMSERVER.extensions_by_name['ext'])
_COMMAND_GETBANHISTORY.extensions_by_name['ext'].message_type = _COMMAND_GETBANHISTORY
ModeratorCommand.RegisterExtension(_COMMAND_GETBANHISTORY.extensions_by_name['ext'])
_COMMAND_WARNUSER.extensions_by_name['ext'].message_type = _COMMAND_WARNUSER
ModeratorCommand.RegisterExtension(_COMMAND_WARNUSER.extensions_by_name['ext'])
_COMMAND_GETWARNHISTORY.extensions_by_name['ext'].message_type = _COMMAND_GETWARNHISTORY
ModeratorCommand.RegisterExtension(_COMMAND_GETWARNHISTORY.extensions_by_name['ext'])
_COMMAND_GETWARNLIST.extensions_by_name['ext'].message_type = _COMMAND_GETWARNLIST
ModeratorCommand.RegisterExtension(_COMMAND_GETWARNLIST.extensions_by_name['ext'])
_COMMAND_VIEWLOGHISTORY.extensions_by_name['ext'].message_type = _COMMAND_VIEWLOGHISTORY
ModeratorCommand.RegisterExtension(_COMMAND_VIEWLOGHISTORY.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
