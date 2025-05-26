from typing import Any
import os


#¿?
from project_db import ProjectDb


#~>
from src.core.errors import TcErr, safe_exec
from src.core.safe_cls import SafeClass
from src.core.result import (
    Result,
    Err,
    Ok,
)


#.?
from .recursive_reader import RecursiveReader
from .errs import ProjectError


#<·
class ProjectSaver(SafeClass):
    def __init__(self, metadata: dict) -> None:
        super().__init__()

        self._metadata: dict = metadata
        self._ignore: list = metadata.get('ignore', [])
        self._path: str = metadata.get('target', '.')

        self._project_dirs: list = []
        self._context: dict = {}

        self.__build()


    def __build(self) -> None:
        for check in (
            self.__validate_parameters,
            self.__create_reader,
            self.__create_record,
        ):
            if ( err := check() ).is_err():
                return self._use_error(err)


    def __create_error(self, msg: str) -> Result[None, ProjectError]:
        return Err(error=ProjectError(
            call='ProjectSaver()',
            source=__name__,
            message=msg
        ))


    def __validate_parameters(self) -> Result[None, ProjectError]:
        if not isinstance(self._path, str) or not self._path:
            return self.__create_error(msg='Invalid parameters')

        return Ok()


    def __create_reader(self) -> Result[None, TcErr]:
        action: RecursiveReader = RecursiveReader(path=self._path, ignore=self._ignore)
        if ( err := action.check_error() ).is_err():
            return err

        self._composition = action.value

        return Ok()


    @safe_exec
    def __create_record(self) -> Any:
        self._value: str = 'project saved succesfully whit ID: '

        entrypoints: str = ''.join(self._metadata.get('entrypoints', []))
        commands: str = ''.join(self._metadata.get('commands', ''))
        langs: str = ''.join(self._metadata.get('langs', ''))
        env: str = ''.join(self._metadata.get('env', ''))

        id_project: int = ProjectDb.add_in(
            composition=self._composition,
            entrypoints=entrypoints,
            commands=commands,
            version=self._metadata.get('version', '0.0.0'),
            langs=langs,
            name=self._metadata.get('project-oficial-name', os.getcwd().split('/')[-1]),
            env=env,
        )

        if not id_project:
            raise ValueError(f'Error creating record, data: {self._metadata}')

        self._value += str(id_project)

    @property
    def value(self) -> str:
        return self._value












