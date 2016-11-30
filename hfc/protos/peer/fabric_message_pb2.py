# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: peer/fabric_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='peer/fabric_message.proto',
  package='protos',
  syntax='proto3',
  serialized_pb=_b('\n\x19peer/fabric_message.proto\x12\x06protos\"\x7f\n\x07Message\x12\"\n\x04type\x18\x01 \x01(\x0e\x32\x14.protos.Message.Type\x12\x0f\n\x07version\x18\x02 \x01(\x05\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\".\n\x04Type\x12\r\n\tUNDEFINED\x10\x00\x12\r\n\tDISCOVERY\x10\x01\x12\x08\n\x04SYNC\x10\x02\x42+Z)github.com/hyperledger/fabric/protos/peerb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_MESSAGE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='protos.Message.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISCOVERY', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYNC', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=118,
  serialized_end=164,
)
_sym_db.RegisterEnumDescriptor(_MESSAGE_TYPE)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='protos.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='protos.Message.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='protos.Message.version', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='protos.Message.payload', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MESSAGE_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=164,
)

_MESSAGE.fields_by_name['type'].enum_type = _MESSAGE_TYPE
_MESSAGE_TYPE.containing_type = _MESSAGE
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGE,
  __module__ = 'peer.fabric_message_pb2'
  # @@protoc_insertion_point(class_scope:protos.Message)
  ))
_sym_db.RegisterMessage(Message)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z)github.com/hyperledger/fabric/protos/peer'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
