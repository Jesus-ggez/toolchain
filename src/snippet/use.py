from typing import Any
import json

#¿?
from snippet_db import SnippetDb, Identifier

#~>
from src.core.safe_cls import SafeClass
from src.core.file_utils import Writer
from src.core.errors import safe_exec
from src.core.result import (
    Ok,
    Result,
)

#.?
from .errs import SnippetError

#<·
class UseSnippet(SafeClass):
    def __init__(self, identifier: str, alias: str) -> None:
        super().__init__()
        self._identifier: str = identifier

        action = self.__read_from_name
        if len(identifier) <= 3 and self._identifier.isalnum():
            action = self.__read_from_id

        res: Result = action()
        if res.is_err():
            self._use_error(res)
            return

        self.create_snippet(alias)


    @safe_exec
    def __read_from_id(self) -> Any:
        v: str = '00' + self._identifier

        _id: int =Identifier.to_number(
            s=v[-3:],
        )
        print(_id)
        self._content: str = SnippetDb.find_by_id(
            id=_id,
        )


    @safe_exec
    def __read_from_name(self) -> Any:
        self._content: str =  SnippetDb.find_by_name(
            name=self._identifier,
        )


    def create_snippet(self, alias: str) -> Result[None, SnippetError]:
        data: dict = json.loads(self._content)

        name: str = data['name']

        if alias != '_':
            name = alias + '.' + name.split('.')[-1]

        creation: Result = Writer().from_str(
            content=data['content'],
            name=name,
        )
        if creation.is_err():
            return creation

        return Ok()
