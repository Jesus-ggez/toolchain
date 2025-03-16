import sys

#<~
from snippet_db import (
    SnippetData,
    Identifier,
    SnippetDb,
)

#~>
from src.core import FileManager


def __cmd_actions(data: list) -> bool:
    if not sys.argv:
        return False

    if sys.argv[0].endswith('.py'):
        return False

    if '--preview' in sys.argv[0]:
        sys.argv.pop(0)
        print(''.join(data))

    return True


def use_template(identifier: str) -> None:
    query = SnippetDb.find_by_name
    value = identifier

    if len(identifier) == 2:
        query = SnippetDb.find_by_id
        value = Identifier.to_number(identifier)

    try:
        record: SnippetData = query(value)

    except Exception as e:
        print(f'Invalid identifier: {identifier}')
        return


    # use metadata
    _raw: str = record.content
    raw: list = _raw.split('<#metadata>')

    _metadata, content = raw


    if __cmd_actions([content]):
        return

    def use_metadata(meta: str, default: str) -> str:
        if '.' in default:
            return default

        extension: str = ''
        stick: str = '->'
        for line in meta.split('\n'):
            if line.strip().startswith('lang'):
                print('ok')
                extension += line.removeprefix('lang' + stick)
                break

        return default + '.' + extension


    title: str = use_metadata(
        default=record.name,
        meta=_metadata,
    )

    FileManager().write.from_str(
        content=content,
        name=title
    )

