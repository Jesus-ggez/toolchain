from typing import NamedTuple


class Lang(NamedTuple):
    import_: str | object
    export: tuple
    conflictive: tuple
    extension: str
    pkg_name: str
    invalid_start: list = [
        '.', '_',
    ]

langs: dict = {
    'py': Lang(
        export=('class', 'def'),
        conflictive=('(', ':'),
        extension='.py',
        pkg_name='__init__.py',
        import_=lambda v0, v1: f'from {v0} import {v1}\n',
    ),
}
