# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: peer/fabric_proposal.proto

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
  name='peer/fabric_proposal.proto',
  package='protos',
  syntax='proto3',
  serialized_pb=_b('\n\x1apeer/fabric_proposal.proto\x12\x06protos\":\n\x0eSignedProposal\x12\x15\n\rproposalBytes\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\">\n\x08Proposal\x12\x0e\n\x06header\x18\x01 \x01(\x0c\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\x12\x11\n\textension\x18\x03 \x01(\x0c\x42+Z)github.com/hyperledger/fabric/protos/peerb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SIGNEDPROPOSAL = _descriptor.Descriptor(
  name='SignedProposal',
  full_name='protos.SignedProposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposalBytes', full_name='protos.SignedProposal.proposalBytes', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature', full_name='protos.SignedProposal.signature', index=1,
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
  serialized_start=38,
  serialized_end=96,
)


_PROPOSAL = _descriptor.Descriptor(
  name='Proposal',
  full_name='protos.Proposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='protos.Proposal.header', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='protos.Proposal.payload', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='extension', full_name='protos.Proposal.extension', index=2,
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
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=98,
  serialized_end=160,
)

DESCRIPTOR.message_types_by_name['SignedProposal'] = _SIGNEDPROPOSAL
DESCRIPTOR.message_types_by_name['Proposal'] = _PROPOSAL

SignedProposal = _reflection.GeneratedProtocolMessageType('SignedProposal', (_message.Message,), dict(
  DESCRIPTOR = _SIGNEDPROPOSAL,
  __module__ = 'peer.fabric_proposal_pb2'
  # @@protoc_insertion_point(class_scope:protos.SignedProposal)
  ))
_sym_db.RegisterMessage(SignedProposal)

Proposal = _reflection.GeneratedProtocolMessageType('Proposal', (_message.Message,), dict(
  DESCRIPTOR = _PROPOSAL,
  __module__ = 'peer.fabric_proposal_pb2'
  # @@protoc_insertion_point(class_scope:protos.Proposal)
  ))
_sym_db.RegisterMessage(Proposal)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z)github.com/hyperledger/fabric/protos/peer'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
