from typing import NamedTuple

#~>


class Lang(NamedTuple): #<·
    import_line: object
    unexport: tuple
    extension: str
    export: tuple
    pkg_name: str
    ignore_file: tuple = ('.', '_')
    kw_export: str | None = None
    conflict: tuple = ()


langs: dict = {
    'py': Lang(
        import_line=lambda i: f'from .{i} import ',
        export=('def', 'class'),
        pkg_name='__init__.py',
        conflict=('(', ':'),
        unexport=('_',),
        extension='.py',
    ),
}
