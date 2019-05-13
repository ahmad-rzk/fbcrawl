from google.protobuf import descriptor_pb2
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import reflection as _reflection
from google.protobuf import message as _message
from google.protobuf import descriptor as _descriptor
import sys
_b = sys.version_info[0] < 3 and (
    lambda x: x) or (lambda x: x.encode('latin1'))
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name='routeguide.proto',
    package='fbcrawl',
    syntax='proto2',
    serialized_pb=_b('\n\x10routeguide.proto\x12\x07\x66\x62\x63rawl\"\xa0\x01\n\x0b\x46\x62\x43rawlItem\x12\x0e\n\x06source\x18\x01 \x02(\t\x12\x0c\n\x04\x64\x61te\x18\x02 \x02(\x03\x12\x0c\n\x04text\x18\x03 \x02(\t\x12\x10\n\x08\x63omments\x18\x04 \x02(\t\x12\x11\n\treactions\x18\x05 \x02(\x03\x12\r\n\x05share\x18\x06 \x02(\t\x12\x0b\n\x03url\x18\x07 \x02(\t\x12\x0f\n\x07post_id\x18\x08 \x02(\t\x12\x13\n\x0bshared_from\x18\t \x02(\t')
)


_FBCRAWLITEM = _descriptor.Descriptor(
    name='FbCrawlItem',
    full_name='fbcrawl.FbCrawlItem',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='source', full_name='fbcrawl.FbCrawlItem.source', index=0,
            number=1, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='date', full_name='fbcrawl.FbCrawlItem.date', index=1,
            number=2, type=3, cpp_type=2, label=2,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='text', full_name='fbcrawl.FbCrawlItem.text', index=2,
            number=3, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='comments', full_name='fbcrawl.FbCrawlItem.comments', index=3,
            number=4, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='reactions', full_name='fbcrawl.FbCrawlItem.reactions', index=4,
            number=5, type=3, cpp_type=2, label=2,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='share', full_name='fbcrawl.FbCrawlItem.share', index=5,
            number=6, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='url', full_name='fbcrawl.FbCrawlItem.url', index=6,
            number=7, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='post_id', full_name='fbcrawl.FbCrawlItem.post_id', index=7,
            number=8, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='shared_from', full_name='fbcrawl.FbCrawlItem.shared_from', index=8,
            number=9, type=9, cpp_type=9, label=2,
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
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=30,
    serialized_end=190,
)

DESCRIPTOR.message_types_by_name['FbCrawlItem'] = _FBCRAWLITEM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FbCrawlItem = _reflection.GeneratedProtocolMessageType('FbCrawlItem', (_message.Message,), dict(
    DESCRIPTOR=_FBCRAWLITEM,
    __module__='routeguide_pb2'
    # @@protoc_insertion_point(class_scope:fbcrawl.FbCrawlItem)
))
_sym_db.RegisterMessage(FbCrawlItem)


# @@protoc_insertion_point(module_scope
