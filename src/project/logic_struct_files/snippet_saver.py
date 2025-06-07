from typing import Any


#¿?
from snippet_db import Identifier
from project_db import ProjectDb


#~>
from src.identity.file_object import FileVO
from src.core.safe_cls import SafeClass
from src.core.errors import safe_exec
from src.core.result import (
    Result,
    Err,
    Ok,
)


#.?
from .errs import ProjectError


#<·
class SnippetSaver(SafeClass):
    def __init__(self, data: FileVO) -> None:
        super().__init__()

        self._value: int = 0

        self._data: FileVO = data

        self.__build()


    def __build(self) -> None:
        for check in (
            self.__validate_parameters,
            self.__use_data,
            self.__create_id,
        ):
            if ( err := check() ).is_err():
                return self._use_error(err)


    def __create_error(self, msg: str) -> Result[None, ProjectError]:
        return Err(error=ProjectError(
            call='SnippetSaver()',
            source=__name__,
            message=msg,
        ))


    def __validate_parameters(self) -> Result[None, ProjectError]:
        if not isinstance(self._data, FileVO):
            return self.__create_error(
                msg=f'Invalid parameters: {self._data} == {type(self._data)}'
            )

        return Ok()


    @safe_exec
    def __use_data(self) -> Any:
        self._value: int = ProjectDb.set_snippet(
            content=self._data.content,
            name=self._data.raw_name,
        )

        if self._value == 0:
            raise Exception('Error saving snippet')


    @safe_exec
    def __create_id(self) -> Any:
        self._repr_value: str = Identifier.from_number(
            num=self._value,
        )

    @property
    def value(self) -> str:
        return self._repr_value
