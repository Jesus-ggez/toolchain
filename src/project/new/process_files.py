from typing import Any


#¿?
from snippet_db import Identifier
from project_db import SnippetDb


#~>
from src.identity.file_object import FileObjectCreator, FileVO
from src.core.safe_cls import SafeClass
from src.core.errors import safe_exec
from src.core.result import (
    Result,
    Err,
    Ok,
)


#.?
from .errs import ProjectError, TcErr


#<·
class ProcessFiles(SafeClass):
    def __init__(self, files: list) -> None:
        super().__init__()

        self._process_content: list = []

        self._files: list = files

        self.__build()


    def __build(self) -> None:
        for check in (
            self.__validate_parameters,
            self.__create_file_valobj, # raw_str -> FileVO
            self.__create_raw_id,      # FileVO -> int
            self.__create_final_id,    # int -> str :: Identifier
        ):
            if ( err := check() ).is_err():
                return self._use_error(err)


    def __create_error(self, msg: str) -> Result[None, TcErr]:
        return Err(error=TcErr(
            call='ProcessFiles()',
            source=__name__,
            message=msg,
        ))


    def __validate_parameters(self) -> Result[None, TcErr]:
        if not isinstance(self._files, list):
            return self.__create_error(msg='Invalid type param')

        return Ok()


    def __create_file_valobj(self) -> Result[None, ProjectError] | Result[None, TcErr]:
        for item in self._files:
            file_valobj: FileObjectCreator = FileObjectCreator(file_name=item)

            if ( err := file_valobj.check_error() ).is_err():
                return err

            self._process_content.append(file_valobj.value)

        return Ok()


    def __create_raw_id(self) -> Result[None, TcErr]:
        data: list = []
        for item in self._process_content:
            record: Result = self.___insert_data(item=item)

            if record.is_err():
                return record

            if record.value == 0:
                return self.__create_error(msg='Snippet insertion failed')

            data.append(record.value)

        self._process_content.clear()
        self._process_content.extend(data)

        return Ok()


    def __create_final_id(self) -> Result[None, TcErr]:
        ids: list = []
        for item in self._process_content:
            str_id: Result = self.___create_identifier(item)

            if str_id.is_err():
                return str_id

            ids.append(str_id.value)

        self._process_content.clear()
        self._process_content.extend(ids)

        return Ok()


    @safe_exec
    def ___insert_data(self, item: FileVO) -> Any:
        return SnippetDb.set_snippet(
            content=item.content,
            name=item.raw_name,
        )


    @safe_exec
    def ___create_identifier(self, item: int) -> Any:
        return Identifier.from_number(item)


    @property
    def value(self) -> list[str]:
        return self._process_content
