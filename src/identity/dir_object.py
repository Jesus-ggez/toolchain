from typing import Any, NamedTuple
import os


#~>
from src.core.errors import safe_exec
from src.core.result import (
    Result,
    Err,
    Ok,
)


#.?
from .struct_value_object import VOIdentity
from .file_object import FileObject, FileVO
from .errs import ValueObjectCreationError


#<·
class DirVO(NamedTuple):
    raw_content: list[str]
    name: str

    content_vo: list[VOIdentity]
    files: list[str]
    dirs: list[str]


class DirObject(VOIdentity):
    def __init__(self, dir_name: str) -> None:
        super().__init__()

        self._model = DirVO

        self._dir_name: str = dir_name.strip()

        self.__build()

        self._create_value_object(
            content_vo=self._content_vo,
            raw_content=self._content,
            files=self._file_names,
            dirs=self._dir_names,
            name=self._dir_name,
        )


    def __build(self) -> None:
        for check in (
            self.__validate_parameters,
            self.__os_move_to_objetive,
            self.__create_content,
            self.__separe_documents,
            self.__create_file_vo_content,
        ):
            if ( err := check() ).is_err():
                return self._use_error(err)


    def __create_error(self, msg: str) -> Result[None, ValueObjectCreationError]:
        return Err(error=ValueObjectCreationError(
            call='DirObject()',
            source=__name__,
            message=msg,
        ))


    def __validate_parameters(self) -> Result[None, ValueObjectCreationError]:
        if not self._dir_name:
            return self.__create_error(msg='Invalid dir name')

        return Ok()


    def __create_content(self) -> Result[None, ValueObjectCreationError]:
        self._content: list = []

        raw_content: Result = self.__os_get_items()
        if raw_content.is_err():
            return raw_content

        if raw_content.value != []:
            self._content.extend(raw_content.value)

        return Ok()


    def __separe_documents(self) -> Result[None, ValueObjectCreationError]:
        self._file_names: list = []
        self._dir_names: list = []

        if not self._content:
            return Ok()

        for item in self._content:
            if os.path.isdir(item):
                self._dir_names.append(item)
                continue

            if os.path.isfile(item):
                self._file_names.append(item)
                continue

            return self.__create_error(msg=f'Unknown document type: {item}')

        return Ok()


    def __create_file_vo_content(self) -> Result[None, ValueObjectCreationError]:
        self._content_vo: list[FileVO] = []
        if not self._file_names:
            return Ok()

        for item in self._file_names:
            raw: FileObject = FileObject(file_name=item)
            if raw.check_error().is_err():
                self._content.append(raw.value)

        return Ok()


    @safe_exec
    def __os_get_items(self) -> Any:
        os.listdir()


    @safe_exec
    def __os_move_to_objetive(self) -> Any:
        os.chdir(self._dir_name)
