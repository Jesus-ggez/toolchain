from snippet_db import (
    SnippetData,
    SnippetDb,
)


def get_all() -> list[SnippetData]:
    try:
        registers: list[SnippetData] = SnippetDb.find_all()
        return registers

    except Exception as e:
        print(e)

    return []
