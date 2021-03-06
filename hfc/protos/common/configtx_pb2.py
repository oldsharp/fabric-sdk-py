# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hfc/protos/common/configtx.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from hfc.protos.common import common_pb2 as hfc_dot_protos_dot_common_dot_common__pb2
from hfc.protos.common import policies_pb2 as hfc_dot_protos_dot_common_dot_policies__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hfc/protos/common/configtx.proto',
  package='hfc.protos.common',
  syntax='proto3',
  serialized_pb=_b('\n hfc/protos/common/configtx.proto\x12\x11hfc.protos.common\x1a\x1ehfc/protos/common/common.proto\x1a hfc/protos/common/policies.proto\"X\n\x0e\x43onfigEnvelope\x12\x0e\n\x06\x63onfig\x18\x01 \x01(\x0c\x12\x36\n\nsignatures\x18\x02 \x03(\x0b\x32\".hfc.protos.common.ConfigSignature\">\n\x0e\x43onfigTemplate\x12,\n\x05items\x18\x01 \x03(\x0b\x32\x1d.hfc.protos.common.ConfigItem\"\xdf\x03\n\x11\x43onfigGroupSchema\x12@\n\x06groups\x18\x01 \x03(\x0b\x32\x30.hfc.protos.common.ConfigGroupSchema.GroupsEntry\x12@\n\x06values\x18\x02 \x03(\x0b\x32\x30.hfc.protos.common.ConfigGroupSchema.ValuesEntry\x12\x44\n\x08policies\x18\x03 \x03(\x0b\x32\x32.hfc.protos.common.ConfigGroupSchema.PoliciesEntry\x1aS\n\x0bGroupsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32$.hfc.protos.common.ConfigGroupSchema:\x02\x38\x01\x1aS\n\x0bValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32$.hfc.protos.common.ConfigValueSchema:\x02\x38\x01\x1aV\n\rPoliciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x34\n\x05value\x18\x02 \x01(\x0b\x32%.hfc.protos.common.ConfigPolicySchema:\x02\x38\x01\"\x13\n\x11\x43onfigValueSchema\"\x14\n\x12\x43onfigPolicySchema\"h\n\x06\x43onfig\x12\x30\n\x06header\x18\x01 \x01(\x0b\x32 .hfc.protos.common.ChannelHeader\x12,\n\x05items\x18\x02 \x03(\x0b\x32\x1d.hfc.protos.common.ConfigItem\"o\n\nConfigNext\x12\x30\n\x06header\x18\x01 \x01(\x0b\x32 .hfc.protos.common.ChannelHeader\x12/\n\x07\x63hannel\x18\x02 \x01(\x0b\x32\x1e.hfc.protos.common.ConfigGroup\"\xda\x03\n\x0b\x43onfigGroup\x12\x0f\n\x07version\x18\x01 \x01(\x04\x12:\n\x06groups\x18\x02 \x03(\x0b\x32*.hfc.protos.common.ConfigGroup.GroupsEntry\x12:\n\x06values\x18\x03 \x03(\x0b\x32*.hfc.protos.common.ConfigGroup.ValuesEntry\x12>\n\x08policies\x18\x04 \x03(\x0b\x32,.hfc.protos.common.ConfigGroup.PoliciesEntry\x12\x12\n\nmod_policy\x18\x05 \x01(\t\x1aM\n\x0bGroupsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12-\n\x05value\x18\x02 \x01(\x0b\x32\x1e.hfc.protos.common.ConfigGroup:\x02\x38\x01\x1aM\n\x0bValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12-\n\x05value\x18\x02 \x01(\x0b\x32\x1e.hfc.protos.common.ConfigValue:\x02\x38\x01\x1aP\n\rPoliciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.hfc.protos.common.ConfigPolicy:\x02\x38\x01\"A\n\x0b\x43onfigValue\x12\x0f\n\x07version\x18\x01 \x01(\x04\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\x12\n\nmod_policy\x18\x03 \x01(\t\"^\n\x0c\x43onfigPolicy\x12\x0f\n\x07version\x18\x01 \x01(\x04\x12)\n\x06policy\x18\x02 \x01(\x0b\x32\x19.hfc.protos.common.Policy\x12\x12\n\nmod_policy\x18\x03 \x01(\t\"\xd9\x01\n\nConfigItem\x12\x36\n\x04type\x18\x01 \x01(\x0e\x32(.hfc.protos.common.ConfigItem.ConfigType\x12\x15\n\rlast_modified\x18\x02 \x01(\x04\x12\x1b\n\x13modification_policy\x18\x03 \x01(\t\x12\x0b\n\x03key\x18\x04 \x01(\t\x12\r\n\x05value\x18\x05 \x01(\x0c\"C\n\nConfigType\x12\n\n\x06POLICY\x10\x00\x12\t\n\x05\x43HAIN\x10\x01\x12\x0b\n\x07ORDERER\x10\x02\x12\x08\n\x04PEER\x10\x03\x12\x07\n\x03MSP\x10\x04\">\n\x0f\x43onfigSignature\x12\x18\n\x10signature_header\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\x42-Z+github.com/hyperledger/fabric/protos/commonb\x06proto3')
  ,
  dependencies=[hfc_dot_protos_dot_common_dot_common__pb2.DESCRIPTOR,hfc_dot_protos_dot_common_dot_policies__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_CONFIGITEM_CONFIGTYPE = _descriptor.EnumDescriptor(
  name='ConfigType',
  full_name='hfc.protos.common.ConfigItem.ConfigType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='POLICY', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHAIN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORDERER', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PEER', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MSP', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1810,
  serialized_end=1877,
)
_sym_db.RegisterEnumDescriptor(_CONFIGITEM_CONFIGTYPE)


_CONFIGENVELOPE = _descriptor.Descriptor(
  name='ConfigEnvelope',
  full_name='hfc.protos.common.ConfigEnvelope',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='hfc.protos.common.ConfigEnvelope.config', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signatures', full_name='hfc.protos.common.ConfigEnvelope.signatures', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=209,
)


_CONFIGTEMPLATE = _descriptor.Descriptor(
  name='ConfigTemplate',
  full_name='hfc.protos.common.ConfigTemplate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='hfc.protos.common.ConfigTemplate.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=211,
  serialized_end=273,
)


_CONFIGGROUPSCHEMA_GROUPSENTRY = _descriptor.Descriptor(
  name='GroupsEntry',
  full_name='hfc.protos.common.ConfigGroupSchema.GroupsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='hfc.protos.common.ConfigGroupSchema.GroupsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='hfc.protos.common.ConfigGroupSchema.GroupsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=499,
  serialized_end=582,
)

_CONFIGGROUPSCHEMA_VALUESENTRY = _descriptor.Descriptor(
  name='ValuesEntry',
  full_name='hfc.protos.common.ConfigGroupSchema.ValuesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='hfc.protos.common.ConfigGroupSchema.ValuesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='hfc.protos.common.ConfigGroupSchema.ValuesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=584,
  serialized_end=667,
)

_CONFIGGROUPSCHEMA_POLICIESENTRY = _descriptor.Descriptor(
  name='PoliciesEntry',
  full_name='hfc.protos.common.ConfigGroupSchema.PoliciesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='hfc.protos.common.ConfigGroupSchema.PoliciesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='hfc.protos.common.ConfigGroupSchema.PoliciesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=669,
  serialized_end=755,
)

_CONFIGGROUPSCHEMA = _descriptor.Descriptor(
  name='ConfigGroupSchema',
  full_name='hfc.protos.common.ConfigGroupSchema',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='groups', full_name='hfc.protos.common.ConfigGroupSchema.groups', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='values', full_name='hfc.protos.common.ConfigGroupSchema.values', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='policies', full_name='hfc.protos.common.ConfigGroupSchema.policies', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CONFIGGROUPSCHEMA_GROUPSENTRY, _CONFIGGROUPSCHEMA_VALUESENTRY, _CONFIGGROUPSCHEMA_POLICIESENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=276,
  serialized_end=755,
)


_CONFIGVALUESCHEMA = _descriptor.Descriptor(
  name='ConfigValueSchema',
  full_name='hfc.protos.common.ConfigValueSchema',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=757,
  serialized_end=776,
)


_CONFIGPOLICYSCHEMA = _descriptor.Descriptor(
  name='ConfigPolicySchema',
  full_name='hfc.protos.common.ConfigPolicySchema',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=778,
  serialized_end=798,
)


_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='hfc.protos.common.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='hfc.protos.common.Config.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='items', full_name='hfc.protos.common.Config.items', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=800,
  serialized_end=904,
)


_CONFIGNEXT = _descriptor.Descriptor(
  name='ConfigNext',
  full_name='hfc.protos.common.ConfigNext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='hfc.protos.common.ConfigNext.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel', full_name='hfc.protos.common.ConfigNext.channel', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=906,
  serialized_end=1017,
)


_CONFIGGROUP_GROUPSENTRY = _descriptor.Descriptor(
  name='GroupsEntry',
  full_name='hfc.protos.common.ConfigGroup.GroupsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='hfc.protos.common.ConfigGroup.GroupsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='hfc.protos.common.ConfigGroup.GroupsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1256,
  serialized_end=1333,
)

_CONFIGGROUP_VALUESENTRY = _descriptor.Descriptor(
  name='ValuesEntry',
  full_name='hfc.protos.common.ConfigGroup.ValuesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='hfc.protos.common.ConfigGroup.ValuesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='hfc.protos.common.ConfigGroup.ValuesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1335,
  serialized_end=1412,
)

_CONFIGGROUP_POLICIESENTRY = _descriptor.Descriptor(
  name='PoliciesEntry',
  full_name='hfc.protos.common.ConfigGroup.PoliciesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='hfc.protos.common.ConfigGroup.PoliciesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='hfc.protos.common.ConfigGroup.PoliciesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1414,
  serialized_end=1494,
)

_CONFIGGROUP = _descriptor.Descriptor(
  name='ConfigGroup',
  full_name='hfc.protos.common.ConfigGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='hfc.protos.common.ConfigGroup.version', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='groups', full_name='hfc.protos.common.ConfigGroup.groups', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='values', full_name='hfc.protos.common.ConfigGroup.values', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='policies', full_name='hfc.protos.common.ConfigGroup.policies', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mod_policy', full_name='hfc.protos.common.ConfigGroup.mod_policy', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CONFIGGROUP_GROUPSENTRY, _CONFIGGROUP_VALUESENTRY, _CONFIGGROUP_POLICIESENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1020,
  serialized_end=1494,
)


_CONFIGVALUE = _descriptor.Descriptor(
  name='ConfigValue',
  full_name='hfc.protos.common.ConfigValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='hfc.protos.common.ConfigValue.version', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='hfc.protos.common.ConfigValue.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mod_policy', full_name='hfc.protos.common.ConfigValue.mod_policy', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1496,
  serialized_end=1561,
)


_CONFIGPOLICY = _descriptor.Descriptor(
  name='ConfigPolicy',
  full_name='hfc.protos.common.ConfigPolicy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='hfc.protos.common.ConfigPolicy.version', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='policy', full_name='hfc.protos.common.ConfigPolicy.policy', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mod_policy', full_name='hfc.protos.common.ConfigPolicy.mod_policy', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1563,
  serialized_end=1657,
)


_CONFIGITEM = _descriptor.Descriptor(
  name='ConfigItem',
  full_name='hfc.protos.common.ConfigItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='hfc.protos.common.ConfigItem.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_modified', full_name='hfc.protos.common.ConfigItem.last_modified', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='modification_policy', full_name='hfc.protos.common.ConfigItem.modification_policy', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key', full_name='hfc.protos.common.ConfigItem.key', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='hfc.protos.common.ConfigItem.value', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONFIGITEM_CONFIGTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1660,
  serialized_end=1877,
)


_CONFIGSIGNATURE = _descriptor.Descriptor(
  name='ConfigSignature',
  full_name='hfc.protos.common.ConfigSignature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='signature_header', full_name='hfc.protos.common.ConfigSignature.signature_header', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature', full_name='hfc.protos.common.ConfigSignature.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1879,
  serialized_end=1941,
)

_CONFIGENVELOPE.fields_by_name['signatures'].message_type = _CONFIGSIGNATURE
_CONFIGTEMPLATE.fields_by_name['items'].message_type = _CONFIGITEM
_CONFIGGROUPSCHEMA_GROUPSENTRY.fields_by_name['value'].message_type = _CONFIGGROUPSCHEMA
_CONFIGGROUPSCHEMA_GROUPSENTRY.containing_type = _CONFIGGROUPSCHEMA
_CONFIGGROUPSCHEMA_VALUESENTRY.fields_by_name['value'].message_type = _CONFIGVALUESCHEMA
_CONFIGGROUPSCHEMA_VALUESENTRY.containing_type = _CONFIGGROUPSCHEMA
_CONFIGGROUPSCHEMA_POLICIESENTRY.fields_by_name['value'].message_type = _CONFIGPOLICYSCHEMA
_CONFIGGROUPSCHEMA_POLICIESENTRY.containing_type = _CONFIGGROUPSCHEMA
_CONFIGGROUPSCHEMA.fields_by_name['groups'].message_type = _CONFIGGROUPSCHEMA_GROUPSENTRY
_CONFIGGROUPSCHEMA.fields_by_name['values'].message_type = _CONFIGGROUPSCHEMA_VALUESENTRY
_CONFIGGROUPSCHEMA.fields_by_name['policies'].message_type = _CONFIGGROUPSCHEMA_POLICIESENTRY
_CONFIG.fields_by_name['header'].message_type = hfc_dot_protos_dot_common_dot_common__pb2._CHANNELHEADER
_CONFIG.fields_by_name['items'].message_type = _CONFIGITEM
_CONFIGNEXT.fields_by_name['header'].message_type = hfc_dot_protos_dot_common_dot_common__pb2._CHANNELHEADER
_CONFIGNEXT.fields_by_name['channel'].message_type = _CONFIGGROUP
_CONFIGGROUP_GROUPSENTRY.fields_by_name['value'].message_type = _CONFIGGROUP
_CONFIGGROUP_GROUPSENTRY.containing_type = _CONFIGGROUP
_CONFIGGROUP_VALUESENTRY.fields_by_name['value'].message_type = _CONFIGVALUE
_CONFIGGROUP_VALUESENTRY.containing_type = _CONFIGGROUP
_CONFIGGROUP_POLICIESENTRY.fields_by_name['value'].message_type = _CONFIGPOLICY
_CONFIGGROUP_POLICIESENTRY.containing_type = _CONFIGGROUP
_CONFIGGROUP.fields_by_name['groups'].message_type = _CONFIGGROUP_GROUPSENTRY
_CONFIGGROUP.fields_by_name['values'].message_type = _CONFIGGROUP_VALUESENTRY
_CONFIGGROUP.fields_by_name['policies'].message_type = _CONFIGGROUP_POLICIESENTRY
_CONFIGPOLICY.fields_by_name['policy'].message_type = hfc_dot_protos_dot_common_dot_policies__pb2._POLICY
_CONFIGITEM.fields_by_name['type'].enum_type = _CONFIGITEM_CONFIGTYPE
_CONFIGITEM_CONFIGTYPE.containing_type = _CONFIGITEM
DESCRIPTOR.message_types_by_name['ConfigEnvelope'] = _CONFIGENVELOPE
DESCRIPTOR.message_types_by_name['ConfigTemplate'] = _CONFIGTEMPLATE
DESCRIPTOR.message_types_by_name['ConfigGroupSchema'] = _CONFIGGROUPSCHEMA
DESCRIPTOR.message_types_by_name['ConfigValueSchema'] = _CONFIGVALUESCHEMA
DESCRIPTOR.message_types_by_name['ConfigPolicySchema'] = _CONFIGPOLICYSCHEMA
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
DESCRIPTOR.message_types_by_name['ConfigNext'] = _CONFIGNEXT
DESCRIPTOR.message_types_by_name['ConfigGroup'] = _CONFIGGROUP
DESCRIPTOR.message_types_by_name['ConfigValue'] = _CONFIGVALUE
DESCRIPTOR.message_types_by_name['ConfigPolicy'] = _CONFIGPOLICY
DESCRIPTOR.message_types_by_name['ConfigItem'] = _CONFIGITEM
DESCRIPTOR.message_types_by_name['ConfigSignature'] = _CONFIGSIGNATURE

ConfigEnvelope = _reflection.GeneratedProtocolMessageType('ConfigEnvelope', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGENVELOPE,
  __module__ = 'hfc.protos.common.configtx_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.common.ConfigEnvelope)
  ))
_sym_db.RegisterMessage(ConfigEnvelope)

ConfigTemplate = _reflection.GeneratedProtocolMessageType('ConfigTemplate', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGTEMPLATE,
  __module__ = 'hfc.protos.common.configtx_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.common.ConfigTemplate)
  ))
_sym_db.RegisterMessage(ConfigTemplate)

ConfigGroupSchema = _reflection.GeneratedProtocolMessageType('ConfigGroupSchema', (_message.Message,), dict(

  GroupsEntry = _reflection.GeneratedProtocolMessageType('GroupsEntry', (_message.Message,), dict(
    DESCRIPTOR = _CONFIGGROUPSCHEMA_GROUPSENTRY,
    __module__ = 'hfc.protos.common.configtx_pb2'
    # @@protoc_insertion_point(class_scope:hfc.protos.common.ConfigGroupSchema.GroupsEntry)
    ))
  ,

  ValuesEntry = _reflection.GeneratedProtocolMessageType('ValuesEntry', (_message.Message,), dict(
    DESCRIPTOR = _CONFIGGROUPSCHEMA_VALUESENTRY,
    __module__ = 'hfc.protos.common.configtx_pb2'
    # @@protoc_insertion_point(class_scope:hfc.protos.common.ConfigGroupSchema.ValuesEntry)
    ))
  ,

  PoliciesEntry = _reflection.GeneratedProtocolMessageType('PoliciesEntry', (_message.Message,), dict(
    DESCRIPTOR = _CONFIGGROUPSCHEMA_POLICIESENTRY,
    __module__ = 'hfc.protos.common.configtx_pb2'
    # @@protoc_insertion_point(class_scope:hfc.protos.common.ConfigGroupSchema.PoliciesEntry)
    ))
  ,
  DESCRIPTOR = _CONFIGGROUPSCHEMA,
  __module__ = 'hfc.protos.common.configtx_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.common.ConfigGroupSchema)
  ))
_sym_db.RegisterMessage(ConfigGroupSchema)
_sym_db.RegisterMessage(ConfigGroupSchema.GroupsEntry)
_sym_db.RegisterMessage(ConfigGroupSchema.ValuesEntry)
_sym_db.RegisterMessage(ConfigGroupSchema.PoliciesEntry)

ConfigValueSchema = _reflection.GeneratedProtocolMessageType('ConfigValueSchema', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGVALUESCHEMA,
  __module__ = 'hfc.protos.common.configtx_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.common.ConfigValueSchema)
  ))
_sym_db.RegisterMessage(ConfigValueSchema)

ConfigPolicySchema = _reflection.GeneratedProtocolMessageType('ConfigPolicySchema', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGPOLICYSCHEMA,
  __module__ = 'hfc.protos.common.configtx_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.common.ConfigPolicySchema)
  ))
_sym_db.RegisterMessage(ConfigPolicySchema)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), dict(
  DESCRIPTOR = _CONFIG,
  __module__ = 'hfc.protos.common.configtx_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.common.Config)
  ))
_sym_db.RegisterMessage(Config)

ConfigNext = _reflection.GeneratedProtocolMessageType('ConfigNext', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGNEXT,
  __module__ = 'hfc.protos.common.configtx_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.common.ConfigNext)
  ))
_sym_db.RegisterMessage(ConfigNext)

ConfigGroup = _reflection.GeneratedProtocolMessageType('ConfigGroup', (_message.Message,), dict(

  GroupsEntry = _reflection.GeneratedProtocolMessageType('GroupsEntry', (_message.Message,), dict(
    DESCRIPTOR = _CONFIGGROUP_GROUPSENTRY,
    __module__ = 'hfc.protos.common.configtx_pb2'
    # @@protoc_insertion_point(class_scope:hfc.protos.common.ConfigGroup.GroupsEntry)
    ))
  ,

  ValuesEntry = _reflection.GeneratedProtocolMessageType('ValuesEntry', (_message.Message,), dict(
    DESCRIPTOR = _CONFIGGROUP_VALUESENTRY,
    __module__ = 'hfc.protos.common.configtx_pb2'
    # @@protoc_insertion_point(class_scope:hfc.protos.common.ConfigGroup.ValuesEntry)
    ))
  ,

  PoliciesEntry = _reflection.GeneratedProtocolMessageType('PoliciesEntry', (_message.Message,), dict(
    DESCRIPTOR = _CONFIGGROUP_POLICIESENTRY,
    __module__ = 'hfc.protos.common.configtx_pb2'
    # @@protoc_insertion_point(class_scope:hfc.protos.common.ConfigGroup.PoliciesEntry)
    ))
  ,
  DESCRIPTOR = _CONFIGGROUP,
  __module__ = 'hfc.protos.common.configtx_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.common.ConfigGroup)
  ))
_sym_db.RegisterMessage(ConfigGroup)
_sym_db.RegisterMessage(ConfigGroup.GroupsEntry)
_sym_db.RegisterMessage(ConfigGroup.ValuesEntry)
_sym_db.RegisterMessage(ConfigGroup.PoliciesEntry)

ConfigValue = _reflection.GeneratedProtocolMessageType('ConfigValue', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGVALUE,
  __module__ = 'hfc.protos.common.configtx_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.common.ConfigValue)
  ))
_sym_db.RegisterMessage(ConfigValue)

ConfigPolicy = _reflection.GeneratedProtocolMessageType('ConfigPolicy', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGPOLICY,
  __module__ = 'hfc.protos.common.configtx_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.common.ConfigPolicy)
  ))
_sym_db.RegisterMessage(ConfigPolicy)

ConfigItem = _reflection.GeneratedProtocolMessageType('ConfigItem', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGITEM,
  __module__ = 'hfc.protos.common.configtx_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.common.ConfigItem)
  ))
_sym_db.RegisterMessage(ConfigItem)

ConfigSignature = _reflection.GeneratedProtocolMessageType('ConfigSignature', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGSIGNATURE,
  __module__ = 'hfc.protos.common.configtx_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.common.ConfigSignature)
  ))
_sym_db.RegisterMessage(ConfigSignature)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z+github.com/hyperledger/fabric/protos/common'))
_CONFIGGROUPSCHEMA_GROUPSENTRY.has_options = True
_CONFIGGROUPSCHEMA_GROUPSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_CONFIGGROUPSCHEMA_VALUESENTRY.has_options = True
_CONFIGGROUPSCHEMA_VALUESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_CONFIGGROUPSCHEMA_POLICIESENTRY.has_options = True
_CONFIGGROUPSCHEMA_POLICIESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_CONFIGGROUP_GROUPSENTRY.has_options = True
_CONFIGGROUP_GROUPSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_CONFIGGROUP_VALUESENTRY.has_options = True
_CONFIGGROUP_VALUESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_CONFIGGROUP_POLICIESENTRY.has_options = True
_CONFIGGROUP_POLICIESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
