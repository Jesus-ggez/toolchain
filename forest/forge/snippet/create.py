import json

#~>
from snippet_db import SnippetDb

#<
class ForceError(Exception): ...


def __extract_metadata(data: list[str], default_name: str) -> dict:
    if '--force' in data[0]:
        raise ForceError('Need version, name, type')

    meta: str = ''.join(data)
    try:
        metadata = json.loads(meta)

    except json.JSONDecodeError:
        raise ValueError('Invalid metadata')

    return {
        'version': metadata.get('version', '0.0.1'),
        'name': metadata.get('name', default_name),
        'type': metadata.get('type', 'test'),
    }


def create_snippet(name: str, reader: type, writer: type) -> None:
    content: list[str] = reader.as_list(name)

    if not content:
        raise ValueError('Empty document')

    #   ···   metadata    ···   #
    _metadata: list[str] = content[:5]

    if ('{' in _metadata[0]):
        content: list[str] = content[6:]

    metadata: dict = __extract_metadata(
        default_name=name,
        data=_metadata,
    )

    SnippetDb.add_in(
        name=metadata['name'],
        version=metadata['version'],
        content=''.join(content),
        _type=metadata['type'],
    )

    writer.write.write_list(
        content=content if not ('{' in _metadata) else content[6:],
        name=name,
    )
