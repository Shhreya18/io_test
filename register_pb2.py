# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: register.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import nanopb_pb2 as nanopb__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eregister.proto\x1a\x0cnanopb.proto\"\xbc\x01\n\x11RegisterInterface\x12%\n\thandshake\x18\x01 \x01(\x0e\x32\x12.RegisterHandshake\x12%\n\toperation\x18\x02 \x01(\x0e\x32\x12.RegisterOperation\x12\r\n\x05\x63ount\x18\x03 \x01(\r\x12\x0f\n\x07\x61\x64\x64ress\x18\x04 \x01(\r\x12\x1c\n\x07payload\x18\x05 \x03(\rB\x0b\x92?\x02\x10@\x92?\x03\x80\x01\x01\x12\x1b\n\x06result\x18\x06 \x03(\rB\x0b\x92?\x02\x10@\x92?\x03\x80\x01\x01*O\n\x11RegisterOperation\x12\x12\n\x0eRO_UNSPECIFIED\x10\x00\x12\x0b\n\x07RO_READ\x10\x01\x12\x0c\n\x08RO_WRITE\x10\x02\x12\x0b\n\x07RO_DONE\x10\x03*B\n\x11RegisterHandshake\x12\x12\n\x0eRH_UNSPECIFIED\x10\x00\x12\x0c\n\x08RH_START\x10\x01\x12\x0b\n\x07RH_DONE\x10\x02\x42\x06\x92?\x03\xa8\x01\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'register_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\222?\003\250\001\001'
  _REGISTERINTERFACE.fields_by_name['payload']._options = None
  _REGISTERINTERFACE.fields_by_name['payload']._serialized_options = b'\222?\002\020@\222?\003\200\001\001'
  _REGISTERINTERFACE.fields_by_name['result']._options = None
  _REGISTERINTERFACE.fields_by_name['result']._serialized_options = b'\222?\002\020@\222?\003\200\001\001'
  _REGISTEROPERATION._serialized_start=223
  _REGISTEROPERATION._serialized_end=302
  _REGISTERHANDSHAKE._serialized_start=304
  _REGISTERHANDSHAKE._serialized_end=370
  _REGISTERINTERFACE._serialized_start=33
  _REGISTERINTERFACE._serialized_end=221
# @@protoc_insertion_point(module_scope)
