# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import document_similarity_out_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='bw2.proto',
  package='',
  serialized_pb='\n\tbw2.proto\x1a\x1d\x64ocument_similarity_out.proto\"\xec\x01\n\x0eProvenanceInfo\x12?\n\x11\x63urrentProvenance\x18\x01 \x02(\x0b\x32$.ProvenanceInfo.SingleProvenanceInfo\x12\x41\n\x13previousProvenances\x18\x02 \x03(\x0b\x32$.ProvenanceInfo.SingleProvenanceInfo\x1aV\n\x14SingleProvenanceInfo\x12 \n\x18lastModificationMarkerId\x18\x01 \x02(\t\x12\x1c\n\x14lastModificationDate\x18\x02 \x02(\x03\"\\\n\x08KeyValue\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\x12\x0f\n\x07\x63omment\x18\x03 \x01(\t\x12#\n\nprovenance\x18\x04 \x01(\x0b\x32\x0f.ProvenanceInfo\"C\n\x10TextWithLanguage\x12\x0c\n\x04text\x18\x01 \x02(\t\x12\x10\n\x08language\x18\x02 \x01(\t\x12\x0f\n\x07\x63omment\x18\x03 \x01(\t\"Q\n\x0b\x43lassifCode\x12\x0e\n\x06source\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x03(\t\x12#\n\nprovenance\x18\x03 \x01(\x0b\x32\x0f.ProvenanceInfo\"d\n\x0b\x41\x66\x66iliation\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\x15\n\raffiliationId\x18\x02 \x02(\t\x12\x0c\n\x04text\x18\x03 \x02(\t\x12#\n\nprovenance\x18\x04 \x01(\x0b\x32\x0f.ProvenanceInfo\"\xdb\x01\n\x06\x41uthor\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\x11\n\tforenames\x18\x02 \x01(\t\x12\x0f\n\x07surname\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\r\n\x05\x65mail\x18\x05 \x01(\t\x12!\n\x0e\x61\x66\x66iliationRef\x18\x06 \x03(\x0b\x32\t.KeyValue\x12\r\n\x05\x64ocId\x18\x07 \x01(\t\x12\x16\n\x0epositionNumber\x18\x08 \x01(\x05\x12\x18\n\x05\x65xtId\x18\t \x03(\x0b\x32\t.KeyValue\x12\x1f\n\x0c\x61uxiliarInfo\x18\n \x03(\x0b\x32\t.KeyValue\"\xe3\x01\n\rBasicMetadata\x12 \n\x05title\x18\x01 \x03(\x0b\x32\x11.TextWithLanguage\x12\x17\n\x06\x61uthor\x18\x02 \x03(\x0b\x32\x07.Author\x12\x0b\n\x03\x64oi\x18\x03 \x01(\t\x12\x0f\n\x07journal\x18\x04 \x01(\t\x12\x0c\n\x04isbn\x18\x05 \x01(\t\x12\x0c\n\x04issn\x18\x06 \x01(\t\x12\x0c\n\x04year\x18\x07 \x01(\t\x12\r\n\x05issue\x18\x08 \x01(\t\x12\x0e\n\x06volume\x18\t \x01(\t\x12\r\n\x05pages\x18\n \x01(\t\x12!\n\x0b\x63lassifCode\x18\x0b \x03(\x0b\x32\x0c.ClassifCode\"v\n\x0cKeywordsList\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x10\n\x08language\x18\x02 \x01(\t\x12\x10\n\x08keywords\x18\x03 \x03(\t\x12\x0f\n\x07\x63omment\x18\x04 \x01(\t\x12#\n\nprovenance\x18\x05 \x01(\x0b\x32\x0f.ProvenanceInfo\"\xa3\x03\n\x10\x44ocumentMetadata\x12\x0b\n\x03key\x18\x01 \x02(\t\x12%\n\rbasicMetadata\x18\x02 \x02(\x0b\x32\x0e.BasicMetadata\x12+\n\x10\x64ocumentAbstract\x18\x03 \x03(\x0b\x32\x11.TextWithLanguage\x12\x1f\n\x08keywords\x18\n \x03(\x0b\x32\r.KeywordsList\x12N\n\x13similarDocumentInfo\x18\x14 \x03(\x0b\x32\x31.pl.edu.icm.coansys.models.DocumentSimilarityInfo\x12\x18\n\x05\x65xtId\x18\x05 \x03(\x0b\x32\t.KeyValue\x12\x1f\n\x0c\x61uxiliarInfo\x18\x06 \x03(\x0b\x32\t.KeyValue\x12\"\n\x0c\x61\x66\x66iliations\x18\x0c \x03(\x0b\x32\x0c.Affiliation\x12%\n\treference\x18\x07 \x03(\x0b\x32\x12.ReferenceMetadata\x12\x12\n\ncollection\x18\x08 \x03(\t\x12\x12\n\nsourcePath\x18\t \x01(\t\x12\x0f\n\x07origKey\x18\x0b \x03(\t\"\x95\x01\n\x11ReferenceMetadata\x12%\n\rbasicMetadata\x18\x01 \x02(\x0b\x32\x0e.BasicMetadata\x12\x14\n\x0csourceDocKey\x18\x02 \x01(\t\x12\x10\n\x08position\x18\x03 \x01(\x05\x12\x17\n\x0frawCitationText\x18\x04 \x01(\t\x12\x18\n\x05\x65xtId\x18\x05 \x03(\x0b\x32\t.KeyValue\"\xb6\x01\n\x05Media\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\x11\n\tmediaType\x18\x02 \x02(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x02(\x0c\x12\x12\n\ncollection\x18\x04 \x01(\t\x12\x12\n\nsourcePath\x18\x05 \x01(\t\x12\x16\n\x0esourceFilesize\x18\x06 \x01(\x03\x12\x17\n\x0f\x64\x65stinationPath\x18\x07 \x01(\t\x12#\n\nprovenance\x18\x08 \x01(\x0b\x32\x0f.ProvenanceInfo\"\'\n\x0eMediaContainer\x12\x15\n\x05media\x18\x01 \x03(\x0b\x32\x06.Media\"v\n\x0f\x44ocumentWrapper\x12\r\n\x05rowId\x18\x01 \x02(\t\x12+\n\x10\x64ocumentMetadata\x18\x02 \x01(\x0b\x32\x11.DocumentMetadata\x12\'\n\x0emediaContainer\x18\x03 \x01(\x0b\x32\x0f.MediaContainerB+\n\x19pl.edu.icm.coansys.modelsB\x0e\x44ocumentProtos')




_PROVENANCEINFO_SINGLEPROVENANCEINFO = descriptor.Descriptor(
  name='SingleProvenanceInfo',
  full_name='ProvenanceInfo.SingleProvenanceInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='lastModificationMarkerId', full_name='ProvenanceInfo.SingleProvenanceInfo.lastModificationMarkerId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='lastModificationDate', full_name='ProvenanceInfo.SingleProvenanceInfo.lastModificationDate', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
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
  extension_ranges=[],
  serialized_start=195,
  serialized_end=281,
)

_PROVENANCEINFO = descriptor.Descriptor(
  name='ProvenanceInfo',
  full_name='ProvenanceInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='currentProvenance', full_name='ProvenanceInfo.currentProvenance', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='previousProvenances', full_name='ProvenanceInfo.previousProvenances', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PROVENANCEINFO_SINGLEPROVENANCEINFO, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=45,
  serialized_end=281,
)


_KEYVALUE = descriptor.Descriptor(
  name='KeyValue',
  full_name='KeyValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='key', full_name='KeyValue.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value', full_name='KeyValue.value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='comment', full_name='KeyValue.comment', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='provenance', full_name='KeyValue.provenance', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  extension_ranges=[],
  serialized_start=283,
  serialized_end=375,
)


_TEXTWITHLANGUAGE = descriptor.Descriptor(
  name='TextWithLanguage',
  full_name='TextWithLanguage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='text', full_name='TextWithLanguage.text', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='language', full_name='TextWithLanguage.language', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='comment', full_name='TextWithLanguage.comment', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=377,
  serialized_end=444,
)


_CLASSIFCODE = descriptor.Descriptor(
  name='ClassifCode',
  full_name='ClassifCode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='source', full_name='ClassifCode.source', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value', full_name='ClassifCode.value', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='provenance', full_name='ClassifCode.provenance', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  extension_ranges=[],
  serialized_start=446,
  serialized_end=527,
)


_AFFILIATION = descriptor.Descriptor(
  name='Affiliation',
  full_name='Affiliation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='key', full_name='Affiliation.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='affiliationId', full_name='Affiliation.affiliationId', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='text', full_name='Affiliation.text', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='provenance', full_name='Affiliation.provenance', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  extension_ranges=[],
  serialized_start=529,
  serialized_end=629,
)


_AUTHOR = descriptor.Descriptor(
  name='Author',
  full_name='Author',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='key', full_name='Author.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='forenames', full_name='Author.forenames', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='surname', full_name='Author.surname', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='name', full_name='Author.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='email', full_name='Author.email', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='affiliationRef', full_name='Author.affiliationRef', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='docId', full_name='Author.docId', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='positionNumber', full_name='Author.positionNumber', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='extId', full_name='Author.extId', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='auxiliarInfo', full_name='Author.auxiliarInfo', index=9,
      number=10, type=11, cpp_type=10, label=3,
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
  extension_ranges=[],
  serialized_start=632,
  serialized_end=851,
)


_BASICMETADATA = descriptor.Descriptor(
  name='BasicMetadata',
  full_name='BasicMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='title', full_name='BasicMetadata.title', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='author', full_name='BasicMetadata.author', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='doi', full_name='BasicMetadata.doi', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='journal', full_name='BasicMetadata.journal', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='isbn', full_name='BasicMetadata.isbn', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='issn', full_name='BasicMetadata.issn', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='year', full_name='BasicMetadata.year', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='issue', full_name='BasicMetadata.issue', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='volume', full_name='BasicMetadata.volume', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pages', full_name='BasicMetadata.pages', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='classifCode', full_name='BasicMetadata.classifCode', index=10,
      number=11, type=11, cpp_type=10, label=3,
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
  extension_ranges=[],
  serialized_start=854,
  serialized_end=1081,
)


_KEYWORDSLIST = descriptor.Descriptor(
  name='KeywordsList',
  full_name='KeywordsList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type', full_name='KeywordsList.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='language', full_name='KeywordsList.language', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='keywords', full_name='KeywordsList.keywords', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='comment', full_name='KeywordsList.comment', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='provenance', full_name='KeywordsList.provenance', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  extension_ranges=[],
  serialized_start=1083,
  serialized_end=1201,
)


_DOCUMENTMETADATA = descriptor.Descriptor(
  name='DocumentMetadata',
  full_name='DocumentMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='key', full_name='DocumentMetadata.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='basicMetadata', full_name='DocumentMetadata.basicMetadata', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='documentAbstract', full_name='DocumentMetadata.documentAbstract', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='keywords', full_name='DocumentMetadata.keywords', index=3,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='similarDocumentInfo', full_name='DocumentMetadata.similarDocumentInfo', index=4,
      number=20, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='extId', full_name='DocumentMetadata.extId', index=5,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='auxiliarInfo', full_name='DocumentMetadata.auxiliarInfo', index=6,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='affiliations', full_name='DocumentMetadata.affiliations', index=7,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='reference', full_name='DocumentMetadata.reference', index=8,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='collection', full_name='DocumentMetadata.collection', index=9,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sourcePath', full_name='DocumentMetadata.sourcePath', index=10,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='origKey', full_name='DocumentMetadata.origKey', index=11,
      number=11, type=9, cpp_type=9, label=3,
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
  extension_ranges=[],
  serialized_start=1204,
  serialized_end=1623,
)


_REFERENCEMETADATA = descriptor.Descriptor(
  name='ReferenceMetadata',
  full_name='ReferenceMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='basicMetadata', full_name='ReferenceMetadata.basicMetadata', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sourceDocKey', full_name='ReferenceMetadata.sourceDocKey', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='position', full_name='ReferenceMetadata.position', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='rawCitationText', full_name='ReferenceMetadata.rawCitationText', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='extId', full_name='ReferenceMetadata.extId', index=4,
      number=5, type=11, cpp_type=10, label=3,
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
  extension_ranges=[],
  serialized_start=1626,
  serialized_end=1775,
)


_MEDIA = descriptor.Descriptor(
  name='Media',
  full_name='Media',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='key', full_name='Media.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='mediaType', full_name='Media.mediaType', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='content', full_name='Media.content', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='collection', full_name='Media.collection', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sourcePath', full_name='Media.sourcePath', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sourceFilesize', full_name='Media.sourceFilesize', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='destinationPath', full_name='Media.destinationPath', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='provenance', full_name='Media.provenance', index=7,
      number=8, type=11, cpp_type=10, label=1,
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
  extension_ranges=[],
  serialized_start=1778,
  serialized_end=1960,
)


_MEDIACONTAINER = descriptor.Descriptor(
  name='MediaContainer',
  full_name='MediaContainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='media', full_name='MediaContainer.media', index=0,
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
  extension_ranges=[],
  serialized_start=1962,
  serialized_end=2001,
)


_DOCUMENTWRAPPER = descriptor.Descriptor(
  name='DocumentWrapper',
  full_name='DocumentWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='rowId', full_name='DocumentWrapper.rowId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='documentMetadata', full_name='DocumentWrapper.documentMetadata', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='mediaContainer', full_name='DocumentWrapper.mediaContainer', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  extension_ranges=[],
  serialized_start=2003,
  serialized_end=2121,
)

_PROVENANCEINFO_SINGLEPROVENANCEINFO.containing_type = _PROVENANCEINFO;
_PROVENANCEINFO.fields_by_name['currentProvenance'].message_type = _PROVENANCEINFO_SINGLEPROVENANCEINFO
_PROVENANCEINFO.fields_by_name['previousProvenances'].message_type = _PROVENANCEINFO_SINGLEPROVENANCEINFO
_KEYVALUE.fields_by_name['provenance'].message_type = _PROVENANCEINFO
_CLASSIFCODE.fields_by_name['provenance'].message_type = _PROVENANCEINFO
_AFFILIATION.fields_by_name['provenance'].message_type = _PROVENANCEINFO
_AUTHOR.fields_by_name['affiliationRef'].message_type = _KEYVALUE
_AUTHOR.fields_by_name['extId'].message_type = _KEYVALUE
_AUTHOR.fields_by_name['auxiliarInfo'].message_type = _KEYVALUE
_BASICMETADATA.fields_by_name['title'].message_type = _TEXTWITHLANGUAGE
_BASICMETADATA.fields_by_name['author'].message_type = _AUTHOR
_BASICMETADATA.fields_by_name['classifCode'].message_type = _CLASSIFCODE
_KEYWORDSLIST.fields_by_name['provenance'].message_type = _PROVENANCEINFO
_DOCUMENTMETADATA.fields_by_name['basicMetadata'].message_type = _BASICMETADATA
_DOCUMENTMETADATA.fields_by_name['documentAbstract'].message_type = _TEXTWITHLANGUAGE
_DOCUMENTMETADATA.fields_by_name['keywords'].message_type = _KEYWORDSLIST
_DOCUMENTMETADATA.fields_by_name['similarDocumentInfo'].message_type = document_similarity_out_pb2._DOCUMENTSIMILARITYINFO
_DOCUMENTMETADATA.fields_by_name['extId'].message_type = _KEYVALUE
_DOCUMENTMETADATA.fields_by_name['auxiliarInfo'].message_type = _KEYVALUE
_DOCUMENTMETADATA.fields_by_name['affiliations'].message_type = _AFFILIATION
_DOCUMENTMETADATA.fields_by_name['reference'].message_type = _REFERENCEMETADATA
_REFERENCEMETADATA.fields_by_name['basicMetadata'].message_type = _BASICMETADATA
_REFERENCEMETADATA.fields_by_name['extId'].message_type = _KEYVALUE
_MEDIA.fields_by_name['provenance'].message_type = _PROVENANCEINFO
_MEDIACONTAINER.fields_by_name['media'].message_type = _MEDIA
_DOCUMENTWRAPPER.fields_by_name['documentMetadata'].message_type = _DOCUMENTMETADATA
_DOCUMENTWRAPPER.fields_by_name['mediaContainer'].message_type = _MEDIACONTAINER
DESCRIPTOR.message_types_by_name['ProvenanceInfo'] = _PROVENANCEINFO
DESCRIPTOR.message_types_by_name['KeyValue'] = _KEYVALUE
DESCRIPTOR.message_types_by_name['TextWithLanguage'] = _TEXTWITHLANGUAGE
DESCRIPTOR.message_types_by_name['ClassifCode'] = _CLASSIFCODE
DESCRIPTOR.message_types_by_name['Affiliation'] = _AFFILIATION
DESCRIPTOR.message_types_by_name['Author'] = _AUTHOR
DESCRIPTOR.message_types_by_name['BasicMetadata'] = _BASICMETADATA
DESCRIPTOR.message_types_by_name['KeywordsList'] = _KEYWORDSLIST
DESCRIPTOR.message_types_by_name['DocumentMetadata'] = _DOCUMENTMETADATA
DESCRIPTOR.message_types_by_name['ReferenceMetadata'] = _REFERENCEMETADATA
DESCRIPTOR.message_types_by_name['Media'] = _MEDIA
DESCRIPTOR.message_types_by_name['MediaContainer'] = _MEDIACONTAINER
DESCRIPTOR.message_types_by_name['DocumentWrapper'] = _DOCUMENTWRAPPER

class ProvenanceInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class SingleProvenanceInfo(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _PROVENANCEINFO_SINGLEPROVENANCEINFO
    
    # @@protoc_insertion_point(class_scope:ProvenanceInfo.SingleProvenanceInfo)
  DESCRIPTOR = _PROVENANCEINFO
  
  # @@protoc_insertion_point(class_scope:ProvenanceInfo)

class KeyValue(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _KEYVALUE
  
  # @@protoc_insertion_point(class_scope:KeyValue)

class TextWithLanguage(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TEXTWITHLANGUAGE
  
  # @@protoc_insertion_point(class_scope:TextWithLanguage)

class ClassifCode(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CLASSIFCODE
  
  # @@protoc_insertion_point(class_scope:ClassifCode)

class Affiliation(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AFFILIATION
  
  # @@protoc_insertion_point(class_scope:Affiliation)

class Author(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AUTHOR
  
  # @@protoc_insertion_point(class_scope:Author)

class BasicMetadata(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BASICMETADATA
  
  # @@protoc_insertion_point(class_scope:BasicMetadata)

class KeywordsList(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _KEYWORDSLIST
  
  # @@protoc_insertion_point(class_scope:KeywordsList)

class DocumentMetadata(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DOCUMENTMETADATA
  
  # @@protoc_insertion_point(class_scope:DocumentMetadata)

class ReferenceMetadata(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REFERENCEMETADATA
  
  # @@protoc_insertion_point(class_scope:ReferenceMetadata)

class Media(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MEDIA
  
  # @@protoc_insertion_point(class_scope:Media)

class MediaContainer(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MEDIACONTAINER
  
  # @@protoc_insertion_point(class_scope:MediaContainer)

class DocumentWrapper(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DOCUMENTWRAPPER
  
  # @@protoc_insertion_point(class_scope:DocumentWrapper)

# @@protoc_insertion_point(module_scope)