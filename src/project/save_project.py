from typing import Any
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
from .save_snippet_project import SnippetProjectSaver
from .errs import MetadataError


#<·
class SaveProject(SafeClass):
    def __init__(self, m: dict) -> None:
        super().__init__()

        self._metadata: dict = m

        self.__build()


    def __build(self) -> None:
        if ( err := self.__validate_parameters() ).is_err():
            return self._use_error(err)


    def __create_error(self, msg: str) -> Result[None, MetadataError]:
        return Err(error=MetadataError(
            call='SaveProject()',
            source=__name__,
            message=msg,
        ))


    def __validate_parameters(self) -> Result[None, MetadataError]:
        if not isinstance(self._metadata, dict) or not self._metadata:
            return self.__create_error(msg='Invalid metadata value')

        return Ok()


    def __move_to_init(self) -> Any:
        if self._metadata.get('target') is None:
            return self.__create_error(msg='Invalid initial point project')

        ...



    def __(self): ...













