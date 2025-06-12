from typing import Any


#¿?
from snippet_db import SnippetDb


#~>
from src.core.safe_cls import SafeClass
from src.core.errors import safe_exec
from src.core.result import (
    Result,
    Err,
    Ok,
)


#.?
from .errs import SnippetError


#<·
class SnippetDiscarder(SafeClass):
    def __init__(self, identifier: str) -> None:
        super().__init__()

        self._identifier: str = identifier

        self.__build()


    def __build(self) -> None:
        ...


    def __validate_exists(self) -> Result[None, SnippetError]:
        ...


    @safe_exec
    def ___validate_from_id(self) -> Any:
        return SnippetDb.
