from typing import NamedTuple


#~>
from src.core.safe_cls import SafeClass
from src.core.file_utils import Reader
from src.core.result import (
    Result,
    Err,
    Ok,
)


#.?
from .errs import ValueObjectCreationError


#<·
class FileVO(NamedTuple):
    raw_name: str
    content: str
    name: str

    extension: str


class FileObjectCreator(SafeClass):
    def __init__(self, file_name: str) -> None:
        super().__init__()

        self._extension_name: str = ''
        self._content: str = ''
        self._name: str = ''

        self._file_name: str = file_name.strip()

        self.__build()

        self._value: FileVO = FileVO(
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
            call='FileObjectCreator()',
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
        if not self.___has_extension():
            return Ok()

        raw_extension: str = self._file_name.split('.')[-1].strip()

        if not raw_extension:
            return self.__create_error(msg='Invalid extension format')

        self._extension_name = raw_extension
        return Ok()


    def ___has_extension(self) -> bool:
        return '.' in self._file_name


    def __create_name(self) -> Result[None, Exception]:
        self._name: str = self._file_name.removesuffix(self._extension_name)

        return Ok()


    @property
    def value(self) -> FileVO:
        return self._value
