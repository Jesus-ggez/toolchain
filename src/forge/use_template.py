#<~
from snippet_db import (
    SnippetData,
    Identifier,
    SnippetDb,
)

#~>
from src.core import FileManager


def use_template(identifier: str) -> None:
    query = SnippetDb.find_by_name
    value = identifier

    if len(identifier) == 2:
        query = SnippetDb.find_by_id
        value = Identifier.to_number(identifier)

    record: SnippetData = query(value)

    FileManager().write.from_str(
        content=record.content,
        name=record.name,#.strip(),
    )

