from typing import Any


#¿?
from project_db import ProjectDb


#~>
from src.core.safe_cls import SafeClass
from src.core.errors import safe_exec
from src.core.result import (
    Result,
    Err,
    Ok,
)


#.?
from .recursive_creator import RecursiveCreator
from .content_creator import ContentCreator
from .errs import UseProjectError, TcErr


#<·
class UseProject(SafeClass):
    def __init__(self, alias: str, identifier: str) -> None:
        super().__init__()

        self._raw_content: str = ''
        self._data: dict = {}

        self._identifier: str = identifier
        self._alias: str = alias


        self.__build()


    def __build(self) -> None:
        for check in (
            self.__validate_parameters,
            self.__generate_query,
            self.__create_raw_content,
            self.__create_content,
            self.__use_content,
        ):
            if ( err := check() ).is_err():
                return self._use_error(err)


    def __create_error(self, msg: str) -> Result[None, UseProjectError]:
        return Err(error=UseProjectError(
            call='UseProject()',
            source=__name__,
            message=msg,
        ))


    def __validate_parameters(self) -> Result[None, UseProjectError]:
        if not isinstance(self._alias, str) or not isinstance(self._identifier, str):
            return self.__create_error(msg='Invalid type parameters')

        if not self._alias or not self._identifier:
            return self.__create_error('Invalid parameters value')

        return Ok()


    # future impl, only id use, impl -> name
    def __generate_query(self) -> Result[None, UseProjectError]:
        self._query = ProjectDb.get_project

        if len(self._identifier) <= 3 and self._identifier.isalnum():
            self._query = type

        return Ok()


    def __create_raw_content(self) -> Result[None, UseProjectError]:
        data: Result = self.___get_data()

        if data.is_err():
            return data

        self._raw_content += data.value

        return Ok()


    def __create_content(self) -> Result[None, UseProjectError] | Result[None, TcErr]:
        action: ContentCreator = ContentCreator(
            alias=self._alias if self._alias != '_' else '',
            data=self._raw_content,
        )

        if ( err := action.check_error() ).is_err():
            return err

        self._data.update ( action.value )
        return Ok()


    def __use_content(self) -> Result[None, UseProjectError] | Result[None, TcErr]:
        if ( err := RecursiveCreator(data=self._data).check_error() ).is_err():
            return err

        return Ok()


    @safe_exec
    def ___get_data(self) -> Any:
        return self._query(self._identifier)
