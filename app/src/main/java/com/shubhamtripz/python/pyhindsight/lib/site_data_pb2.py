# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: site_data.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fsite_data.proto\"K\n\x14SiteDataFeatureProto\x12\x1c\n\x14observation_duration\x18\x01 \x01(\x03\x12\x15\n\ruse_timestamp\x18\x02 \x01(\x03\"r\n\x1eSiteDataPerformanceMeasurement\x12\x18\n\x10\x61vg_cpu_usage_us\x18\x01 \x01(\x02\x12\x18\n\x10\x61vg_footprint_kb\x18\x02 \x01(\x02\x12\x1c\n\x14\x61vg_load_duration_us\x18\x03 \x01(\x02\"\xe1\x02\n\rSiteDataProto\x12\x13\n\x0blast_loaded\x18\x01 \x01(\r\x12<\n\x1dupdates_favicon_in_background\x18\x02 \x01(\x0b\x32\x15.SiteDataFeatureProto\x12:\n\x1bupdates_title_in_background\x18\x03 \x01(\x0b\x32\x15.SiteDataFeatureProto\x12\x37\n\x18uses_audio_in_background\x18\x04 \x01(\x0b\x32\x15.SiteDataFeatureProto\x12J\n+deprecated_uses_notifications_in_background\x18\x05 \x01(\x0b\x32\x15.SiteDataFeatureProto\x12<\n\x13load_time_estimates\x18\x06 \x01(\x0b\x32\x1f.SiteDataPerformanceMeasurementB\x02H\x03')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'site_data_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'H\003'
  _globals['_SITEDATAFEATUREPROTO']._serialized_start=19
  _globals['_SITEDATAFEATUREPROTO']._serialized_end=94
  _globals['_SITEDATAPERFORMANCEMEASUREMENT']._serialized_start=96
  _globals['_SITEDATAPERFORMANCEMEASUREMENT']._serialized_end=210
  _globals['_SITEDATAPROTO']._serialized_start=213
  _globals['_SITEDATAPROTO']._serialized_end=566
# @@protoc_insertion_point(module_scope)