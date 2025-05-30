from typing import Any
import json


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
class ListContent(SafeClass):
    def __init__(self) -> None:
        super().__init__()

        self.__build()


    def __build(self) -> None:
        if ( err := self.__get_records() ).is_err():
            return self._use_error(err)

        if ( err := self.__create_visual_repr() ).is_err():
            return self._use_error(err)


    @safe_exec
    def __get_records(self) -> Any:
        data: str = SnippetDb.find_all()

        self._data: list = json.loads(data)


    def __create_visual_repr(self) -> Result[None, SnippetError]:
        basic_repr = lambda name, id_, type_: f'| {name:^10} | {id_:^8} | {type_:^10} |'

        final_repr: str = '|    name    |    id    |    type    |\n'
        div_line: str = '-' * (len(final_repr) - 1)

        final_repr = div_line + '\n' + final_repr + div_line + '\n'

        for item in self._data:
            final_repr += basic_repr(name=item['name'], id_=item['id'], type_=item['type_']) + '\n'

        self._value = final_repr

        return Ok()

    @property
    def value(self) -> str:
        return self._value


