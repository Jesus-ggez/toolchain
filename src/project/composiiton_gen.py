from typing import Any


#~>
from src.core.safe_cls import SafeClass
from src.core.errors import safe_exec
from src.core.result import (
    Result,
    Err,
    Ok,
)


#¿?
from snippet_db import Identifier


#.?
from .errs import MetadataError


#<·
class CompositionGenerator(SafeClass):
    def __init__(self, dir_name: str, dir_content: list[int]) -> None:
        super().__init__()

        self._dir_content: list[int] = dir_content
        self._dir_name: str = dir_name.strip()
        self._identifiers: list[str] = []

        self.__build()


    def __build(self) -> None:
        for check in (
            self.__validate_parameters,
            self.__create_composition_id,
            self.__create_composition,
        ):
            if ( err := check() ).is_err():
                return self._use_error(err)


    def __create_error(self, msg: str) -> Result[None, MetadataError]:
        return Err(error=MetadataError(
            call='CompositionGenerator()',
            source=__name__,
            message=msg,
        ))


    def __validate_parameters(self) -> Result[None, MetadataError]:
        is_invalid_dir_name: bool = not self._dir_name
        is_invalid_dir_content: bool = not isinstance(self._dir_content, list)

        if is_invalid_dir_name or is_invalid_dir_content:
            return self.__create_error(msg='Invalid parameters')

        return Ok()


    def __create_composition_id(self) -> Result[None, MetadataError]:
        self._ids: list[str] = []

        for item_id in self._dir_content:
            if not isinstance(item_id, int) or not item_id:
                return self.__create_error(msg=f'Invalid type value: {item_id} == {type(item_id)}')

            raw: Result = self.__dot_create_file_id(id_=item_id)
            if raw.is_err():
                return raw

            self._ids.append(raw.value)

        return Ok()


    def __create_composition(self) -> Result[None, MetadataError]:
        if not self._ids:
            self._value: str = self._dir_name + '[]'
            return Ok()

        self._value: str = self._dir_name + '[' + ','.join(self._ids) + ']'

        return Ok()


    def __dot_create_file_id(self, id_: int) -> Result[int, MetadataError]:
        gen_id: Result = self.__safe_use_identifier(id_=id_)
        if gen_id.is_err():
            return gen_id

        return Ok(gen_id.value)


    @safe_exec
    def __safe_use_identifier(self, id_: int) -> Any:
        return Identifier.from_number(
            num=id_,
        )


    @property
    def value(self) -> str:
        return self._value
