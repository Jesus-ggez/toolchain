from typing import NamedTuple


#~>
from src.core.file_utils import Reader
from src.core.result import (
    Result,
    Err,
    Ok,
)


#.?
from .struct_value_object import VOIdentity
from .errs import ValueObjectCreationError


#<·
class FileVO(NamedTuple):
    raw_name: str
    content: str
    name: str

    extension: str


class FileObject(VOIdentity):
    def __init__(self, file_name: str) -> None:
        super().__init__()
        self._model = FileVO

        self._file_name: str = file_name.strip()

        self.__build()

        self._create_value_object(
            extension=self._extension_name,
            raw_name=self._file_name,
            content=self._content,
            name=self._name,
        )


    def __build(self) -> None:
        for check in (
            self.__validate_parameters,
            self.__create_content,
            self.__create_extension,
            self.__create_name,
        ):
            if ( err := check() ).is_err():
                return self._use_error(err)


    def __create_error(self, msg: str) -> Result[None, ValueObjectCreationError]:
        return Err(error=ValueObjectCreationError(
            call='FileObject',
            source=__name__,
            message=msg,
        ))


    def __validate_parameters(self) -> Result[None, ValueObjectCreationError]:
        if not self._file_name:
            return self.__create_error(msg='Invalid file name')

        return Ok()


    def __create_content(self) -> Result[None, ValueObjectCreationError]:
        raw_data: Result = Reader.as_str(filename=self._file_name)

        if raw_data.is_err():
            return raw_data

        if not raw_data.value.strip():
            return self.__create_error(msg='File must not be empty')

        self._content: str = raw_data.value.strip()
        return Ok()


    def __create_extension(self) -> Result[None, ValueObjectCreationError]:
        self._extension_name: str = ''

        if not self.__has_extension():
            return Ok()

        raw_extension: str = self._file_name.split('.')[-1]

        if not raw_extension.strip():
            return self.__create_error(msg='Invalid extension format')

        self._extension_name = raw_extension.strip()
        return Ok()


    def __has_extension(self) -> bool:
        return '.' in self._file_name


    def __create_name(self) -> Result[None, Exception]:
        self._name: str = self._file_name.removesuffix(self._extension_name)

        return Ok()
