from typing import Any
import json


#~>
from src.core.safe_cls import SafeClass
from src.core.errors import safe_exec
from src.core.result import (
    Result,
    Err,
    Ok,
)


#¿?
from snippet_db import Identifier
from project_db import ProjectDb


#.?
from .content_generator import ContentGenerator
from .errs import TcErr, UseError


#<·
class ProjectUseWorkspace(SafeClass):
    def __init__(self, identifier: str, alias: str) -> None:
        super().__init__()

        self._identifier: str = identifier.strip()
        self._alias: str = alias

        self.__build()


    def __build(self) -> None:
        if ( err := self.__validate_parameters() ).is_err():
            return self._use_error(err)

        if ( err := self.__create_project() ).is_err():
            return self._use_error(err)


    def __create_error(self, msg: str) -> Result[None, UseError]:
        return Err(error=UseError(
            call='ProjectUseWorkspace()',
            source=__name__,
            message=msg,
        ))


    def __validate_parameters(self) -> Result[None, UseError]:
        if not self._identifier:
            return self.__create_error(msg='Invalid identifier')

        return Ok()


    def __create_project(self) -> Result[None, TcErr] | Result[None, UseError]:
        project: Result = self.___get_project()

        if project.is_err():
            return project

        if not project.value:
            return self.__create_error(msg='Project not found')

        project_data: dict = json.loads(project.value)

        if ( err := ContentGenerator(struct=project_data['composition']).check_error() ).is_err():
            return err

        return Ok()


    @safe_exec
    def ___get_project(self) -> Any:
        if not self._identifier.isalnum():
            return ProjectDb.get_by_name(self._identifier)

        if len(self._identifier) > 3:
            return ProjectDb.get_by_name(self._identifier)


        v: str = '00' + self._identifier
        _id: int =Identifier.to_number(s=v[-3:])
        return ProjectDb.get_by_id(_id)

