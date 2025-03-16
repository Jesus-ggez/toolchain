import sys

#<~
from snippet_db import SnippetDb

#~>
from src.core import FileManager


def __use_rule(base: str, tags: list, action: dict) -> bool:
    for tag in tags:
        if base.strip().startswith(f'__{tag}__'):
            action[tag] = base.split(':')[-1].strip()
            return True

    return False


def __cmd_actions(data: list) -> bool:
    if not sys.argv:
        return False

    if sys.argv[0].endswith('.py'):
        return False

    if '--preview' in sys.argv[0]:
        sys.argv.pop(0)
        print(''.join(data))

    return True


def create_template(tempname: str) -> None:
    meta: dict = {}
    new_doc: list = []

    for line in FileManager().read.as_list(tempname):
        if __use_rule(
            base=line,
            tags=[
                'version',
                'type',
                'name',
            ],
            action=meta,
        ):
            continue

        new_doc.append(line)


    new_name: list = tempname.split('.')
    # metadata
    __metadata: list = [
        'lang->' + new_name[-1],
    ]

    __metadata.append('<#metadata>')
    content: list[str] = __metadata + new_doc

    # terminal actions
    if __cmd_actions(data=content):
        return

    SnippetDb.add_in(
        name=meta.get('name', new_name[0]),
        version=meta.get('version', '0.0.1'),
        _type=meta.get('type', 'base'),
        content=''.join(content),
    )

    FileManager().write.from_list(
        content=new_doc,
        name=tempname,
    )


