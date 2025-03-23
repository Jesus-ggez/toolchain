import os

#~>
from .errors import SnippetMetaError, SnippetMetaImplError
from utils.result import (
    Result,
    Err,
    Ok,
)


class SnippetMeta:
    def __validate(self, document: list) -> Result[None, SnippetMetaError]:
        if document[0] == '#·':
            return Ok()
