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
    serialized_pb=_b('\n\x10routeguide.proto\x12\x07\x66\x62\x63rawl\"\x7f\n\x0b\x43ommentItem\x12\x0e\n\x06source\x18\x01 \x02(\t\x12\x10\n\x08reply_to\x18\x02 \x02(\t\x12\x0c\n\x04\x64\x61te\x18\x03 \x02(\x03\x12\x0c\n\x04text\x18\x04 \x02(\t\x12\x11\n\treactions\x18\x05 \x02(\x03\x12\x12\n\nsource_url\x18\x06 \x02(\t\x12\x0b\n\x03url\x18\x07 \x02(\t')
)


_COMMENTITEM = _descriptor.Descriptor(
    name='CommentItem',
    full_name='fbcrawl.CommentItem',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='source', full_name='fbcrawl.CommentItem.source', index=0,
            number=1, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='reply_to', full_name='fbcrawl.CommentItem.reply_to', index=1,
            number=2, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='date', full_name='fbcrawl.CommentItem.date', index=2,
            number=3, type=3, cpp_type=2, label=2,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='text', full_name='fbcrawl.CommentItem.text', index=3,
            number=4, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='reactions', full_name='fbcrawl.CommentItem.reactions', index=4,
            number=5, type=3, cpp_type=2, label=2,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='source_url', full_name='fbcrawl.CommentItem.source_url', index=5,
            number=6, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='url', full_name='fbcrawl.CommentItem.url', index=6,
            number=7, type=9, cpp_type=9, label=2,
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
    serialized_start=29,
    serialized_end=156,
)

DESCRIPTOR.message_types_by_name['CommentItem'] = _COMMENTITEM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CommentItem = _reflection.GeneratedProtocolMessageType('CommentItem', (_message.Message,), dict(
    DESCRIPTOR=_COMMENTITEM,
    __module__='routeguide_pb2'
    # @@protoc_insertion_point(class_scope:fbcrawl.CommentItem)
))
_sym_db.RegisterMessage(CommentItem)


# @@protoc_insertion_point(module_scope)
