from typing import Any


#¿?
from project_db import ProjectDb


#~>
from src.core.errors import TcErr, safe_exec
from src.core.safe_cls import SafeClass
from src.core.result import (
    Result,
    Ok,
)


#.?
from .dfs import RecursiveReader


#<·
class ProjectSaver(SafeClass):
    def __init__(self, metadata: dict) -> None:
        super().__init__()

        self._metadata: dict = metadata

        self._project_dirs: list = []
        self._context: dict = {}

        self.__build()


    def __build(self) -> None:
        if ( err := self.__create_reader() ).is_err():
            return self._use_error(err)

        if ( err := self.__create_record() ).is_err():
            return self._use_error(err)


    def __create_reader(self) -> Result[None, TcErr]:
        action: RecursiveReader = RecursiveReader(
            ignore=self._metadata.get('ignore', []),
            path=self._metadata.get('target', '.')
        )
        if ( err := action.check_error() ).is_err():
            return err

        self._composition = action.value

        return Ok()


    @safe_exec
    def __create_record(self) -> Any:
        self._value: str = ''

        entrypoints: str = ''.join(self._metadata.get('entrypoints', []))
        commands: str = ''.join(self._metadata.get('commands', ''))
        langs: str = ''.join(self._metadata.get('langs', ''))
        env: str = ''.join(self._metadata.get('env', ''))
        default_version: str = '0.0.0'

        if not self._metadata.get('project-oficial-name'):
            raise ValueError('Needs name to create project')

        id_project: int = ProjectDb.add_in(
            composition=self._composition,
            entrypoints=entrypoints,
            commands=commands,
            version=self._metadata.get('version', default_version),
            langs=langs,
            name=self._metadata['project-oficial-name'],
            env=env,
        )

        if id_project:
            self._value += 'project saved succesfully whit ID: ' + str(id_project)

    @property
    def value(self) -> str:
        return self._value


