#<~
from snippet_db import SnippetDb

#~>
from src.core import FileManager


def __use_rule(base: str, tags: list, action: dict) -> bool:
    for tag in tags:
        if base.startswith(f'__{tag}__'):
            action[tag] = base.split(':')[-1]
            return True

    return False



def create_template(tempname: str) -> None:
    print('creando')
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

    SnippetDb.add_in(
        name=tempname,
        version=meta.get('version', '0.0.1'),
        _type=meta.get('type', 'base'),
        content=''.join(new_doc),
    )

    FileManager().write.from_list(
        content=new_doc,
        name=tempname,
    )


