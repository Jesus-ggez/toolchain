from snippet_db import (
    SnippetData,
    Identifier,
    SnippetDb,
)


def get_snippet(identifier: str) -> dict:
    if len(identifier) == 2:
        _id: int = Identifier.to_numer(identifier)
        record: SnippetData = SnippetDb.find_by_id(
            id=_id,
        )

        return record

    record: SnippetData = SnippetDb.find_by_name(
        name=identifier,
    )
    return record
