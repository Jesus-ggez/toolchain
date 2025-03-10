from snippet_db import (
    Identifier,
    SnippetDb,
)


def disable_snippet(id: str) -> None:
    _id: int = Identifier.to_number(id)
    try:
        SnippetDb.discard(_id)
        print('Snippet Deleted')

    except Exception as e:
        print(e)
