# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/news_bot.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15protos/news_bot.proto\x12\x05groom\x1a\x1fgoogle/protobuf/timestamp.proto\"M\n\tNewsFlash\x12-\n\tnews_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x11\n\tnews_item\x18\x02 \x01(\t\"#\n\x10NewsStreamStatus\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\x46\n\x05Groom\x12=\n\x0eSendNewsStream\x12\x10.groom.NewsFlash\x1a\x17.groom.NewsStreamStatus(\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.news_bot_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_NEWSFLASH']._serialized_start=65
  _globals['_NEWSFLASH']._serialized_end=142
  _globals['_NEWSSTREAMSTATUS']._serialized_start=144
  _globals['_NEWSSTREAMSTATUS']._serialized_end=179
  _globals['_GROOM']._serialized_start=181
  _globals['_GROOM']._serialized_end=251
# @@protoc_insertion_point(module_scope)