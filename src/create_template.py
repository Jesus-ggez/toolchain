from snippet_db import SnippetDb

#~>
try:
    from snippet_rules import SnippetRules

except:
    from .snippet_rules import SnippetRules


def create_template(data: list[str], tempname: str) -> None:
    meta: dict = {}
    new_doc: list = []

    for line in data:
        if line.startswith(SnippetRules.VERSION):
            meta['version'] = line.removeprefix(SnippetRules.VERSION)
            continue

        if SnippetRules.IGNORE in line:
            continue

        if line.startswith(SnippetRules.TYPE):
            meta['type'] = line.removeprefix(SnippetRules.TYPE)
            continue

        new_doc.append(line)


    SnippetDb.add_in(
        name=tempname,
        version=meta.get('version', '0.0.1'),
        content=''.join(new_doc),
        _type=meta.get('type', 'base')
    )
