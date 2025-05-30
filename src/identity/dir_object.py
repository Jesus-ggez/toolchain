from typing import Any, NamedTuple
import os


#~>
from src.core.safe_cls import SafeClass
from src.core.errors import safe_exec
from src.core.result import (
    Result,
    Err,
    Ok,
)


#.?
from .errs import ValueObjectCreationError


#<·
class DirVO(NamedTuple):
    name: str
    raw_content: list[str]
    files: list[str]
    dirs: list[str]


class DirObjectCreator(SafeClass):
    def __init__(self, dir_name: str) -> None:
        super().__init__()

        self._file_names: list[str] = []
        self._dir_names: list[str] = []
        self._content: list[str] = []

        self._dir_name: str = dir_name.strip()

        self.__build()

        self._value: DirVO = DirVO(
            raw_content=self._content,
            files=self._file_names,
            dirs=self._dir_names,
            name=self._dir_name,
        )


    def __build(self) -> None:
        for check in (
            self.__validate_parameters,
            self.__move_to_objetive,
            self.__create_content,
            self.__separe_documents,
        ):
            if ( err := check() ).is_err():
                return self._use_error(err)


    def __create_error(self, msg: str) -> Result[None, ValueObjectCreationError]:
        return Err(error=ValueObjectCreationError(
            call='DirObjectCreator()',
            source=__name__,
            message=msg,
        ))


    def __validate_parameters(self) -> Result[None, ValueObjectCreationError]:
        if not self._dir_name:
            return self.__create_error(msg='Invalid dir name')

        return Ok()


    def __create_content(self) -> Result[None, ValueObjectCreationError]:
        raw_content: Result = self.___get_items()
        if raw_content.is_err():
            return raw_content

        self._content.extend(raw_content.value)
        return Ok()


    def __separe_documents(self) -> Result[None, ValueObjectCreationError]:
        if not self._content:
            return Ok()

        for item in self._content:
            if os.path.isdir(item):
                self._dir_names.append(item)
                continue

            if os.path.isfile(item):
                self._file_names.append(item)
                continue

        return Ok()


    @safe_exec
    def ___get_items(self) -> Any:
        return os.listdir()


    @safe_exec
    def __move_to_objetive(self) -> Any:
        return os.chdir(self._dir_name)


    @property
    def value(self) -> DirVO:
        return self._value
