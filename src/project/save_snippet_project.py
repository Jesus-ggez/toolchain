from typing import Any


#¿?
from project_db import ProjectDb


#~>
from src.core.safe_cls import SafeClass
from src.core.file_utils import Reader
from src.core.errors import safe_exec
from src.core.result import (
    Result,
    Err,
    Ok,
)


#.?
from .errs import MetadataError


#<·
class SnippetProjectSaver(SafeClass):
    def __init__(self, snippet_name: str) -> None:
        super().__init__()

        self._snippet_name: str = snippet_name.strip()
        self._value_id: int = 0

        self.__build()


    def __build(self) -> None:
        if ( err := self.__validate_parameters() ).is_err():
            return self._use_error(err)

        if ( err := self.__get_file_content() ).is_err():
            return self._use_error(err)

        if ( err := self.__create_record() ).is_err():
            return self._use_error(err)


    def __create_error(self, msg: str) -> Result[None, MetadataError]:
        return Err(error=MetadataError(
            call='SnippetProjectSaver()',
            source=__name__,
            message=msg,
        ))


    def __validate_parameters(self) -> Result[None, MetadataError]:
        if not self._snippet_name:
            return self.__create_error(msg='Invalid name for read')

        return Ok()


    def __get_file_content(self) -> Result[None, MetadataError]:
        raw_data: Result = Reader.as_str(self._snippet_name)
        if raw_data.is_err():
            return raw_data

        data: str = raw_data.value.strip()
        if not data:
            return self.__create_error(msg='Invalid snippet content')

        self._file_content: str = data
        return Ok()


    @safe_exec
    def __create_record(self) -> Any:
        self._value_id += ProjectDb.set_snippet(
            content=self._file_content,
            name=self._snippet_name,
        )


    @property
    def value_id(self) -> int:
        return self._value_id
