from typing import Any
import os


#¿?
from snippet_db import SnippetDb


#~>
from src.core.errors import TcErr, safe_exec
from src.tcfmt.constants import TcConfig
from src.core.safe_cls import SafeClass
from src.core.file_utils import Reader
from src.core.result import (
    Result,
    Err,
    Ok,
)


#.?
from .errs import MetadataError


#<·
class SnippetSaver(SafeClass):
    def __init__(self, metadata: dict) -> None:
        super().__init__()

        self._metadata: dict = metadata

        self.__build()


    def __build(self) -> None:
        if ( err := self.__validate_metadata() ).is_err():
            return self._use_error(err)

        if ( err := self.__create_data() ).is_err():
            return self._use_error(err)

        if ( err := self.__create_record() ).is_err():
            return self._use_error(err)

        if ( err := self.__remove_document() ).is_err():
            return self._use_error(err)


    def __validate_metadata(self) -> Result[None, MetadataError]:
        required_keys: set = { 'target', 'name' }

        if ( missing := (required_keys - self._metadata.keys()) ):
            print(missing)
            return Err(error=MetadataError(
                message='Missing keys to add metadata',
                call='save_snippet()',
                source=__name__,
            ))

        return Ok()


    def __create_data(self) -> Result[None, TcErr]:
        data: Result = Reader.as_str(filename=self._metadata['target'])

        if data.is_ok():
            self._data: str = data.value
            return Ok()

        return data


    @safe_exec
    def __create_record(self) -> Any:
        self.__value = SnippetDb.add_in(
            name=self._metadata['name'] + '.' + self._metadata.get('lang', 'txt'),
            version=self._metadata.get('version', '0.0.0'),
            _type=self._metadata.get('type', 'test'),
            content=self._data,
        )


    @safe_exec
    def __remove_document(self) -> Any:
        return os.remove(TcConfig.FILE_NAME)


    @property
    def value(self) -> Any:
        return self.__value
