# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: delf/protos/feature.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from delf.protos import datum_pb2 as delf_dot_protos_dot_datum__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='delf/protos/feature.proto',
  package='delf.protos',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x19\x64\x65lf/protos/feature.proto\x12\x0b\x64\x65lf.protos\x1a\x17\x64\x65lf/protos/datum.proto\"\x86\x01\n\x0b\x44\x65lfFeature\x12+\n\ndescriptor\x18\x01 \x01(\x0b\x32\x17.delf.protos.DatumProto\x12\t\n\x01x\x18\x02 \x01(\x02\x12\t\n\x01y\x18\x03 \x01(\x02\x12\r\n\x05scale\x18\x04 \x01(\x02\x12\x13\n\x0borientation\x18\x05 \x01(\x02\x12\x10\n\x08strength\x18\x06 \x01(\x02\"9\n\x0c\x44\x65lfFeatures\x12)\n\x07\x66\x65\x61ture\x18\x01 \x03(\x0b\x32\x18.delf.protos.DelfFeature')
  ,
  dependencies=[delf_dot_protos_dot_datum__pb2.DESCRIPTOR,])




_DELFFEATURE = _descriptor.Descriptor(
  name='DelfFeature',
  full_name='delf.protos.DelfFeature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='descriptor', full_name='delf.protos.DelfFeature.descriptor', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='x', full_name='delf.protos.DelfFeature.x', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='delf.protos.DelfFeature.y', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scale', full_name='delf.protos.DelfFeature.scale', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orientation', full_name='delf.protos.DelfFeature.orientation', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strength', full_name='delf.protos.DelfFeature.strength', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
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
  serialized_end=202,
)


_DELFFEATURES = _descriptor.Descriptor(
  name='DelfFeatures',
  full_name='delf.protos.DelfFeatures',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature', full_name='delf.protos.DelfFeatures.feature', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
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
  serialized_start=204,
  serialized_end=261,
)

_DELFFEATURE.fields_by_name['descriptor'].message_type = delf_dot_protos_dot_datum__pb2._DATUMPROTO
_DELFFEATURES.fields_by_name['feature'].message_type = _DELFFEATURE
DESCRIPTOR.message_types_by_name['DelfFeature'] = _DELFFEATURE
DESCRIPTOR.message_types_by_name['DelfFeatures'] = _DELFFEATURES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DelfFeature = _reflection.GeneratedProtocolMessageType('DelfFeature', (_message.Message,), dict(
  DESCRIPTOR = _DELFFEATURE,
  __module__ = 'delf.protos.feature_pb2'
  # @@protoc_insertion_point(class_scope:delf.protos.DelfFeature)
  ))
_sym_db.RegisterMessage(DelfFeature)

DelfFeatures = _reflection.GeneratedProtocolMessageType('DelfFeatures', (_message.Message,), dict(
  DESCRIPTOR = _DELFFEATURES,
  __module__ = 'delf.protos.feature_pb2'
  # @@protoc_insertion_point(class_scope:delf.protos.DelfFeatures)
  ))
_sym_db.RegisterMessage(DelfFeatures)


# @@protoc_insertion_point(module_scope)
