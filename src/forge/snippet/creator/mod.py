import os


#~>
from src.utils.base_safe import SafeClass
from .errors import CreatorManagerError
from src.core import FileManager
from .app import SnippetCreator
from utils.result import (
    Result,
    Err,
    Ok,
)


class CreatorManager(SafeClass):
    def __init__(self, data: dict) -> None:
        self.name: str = self.__class__.__name__
        self._data: dict = data

        super().__init__()

        self.basic: tuple = (
            'version',
            'name',
            'target',
            'type',
        )

        check: Result = self.__exists()
        if check.is_err():
            self._use_error(check)
            return

        creator: Result = self.get_content()
        if creator.is_err():
            self._use_error(creator)
            return

        actor: SnippetCreator = SnippetCreator(content=self._data)
        if ( err := actor.check_error() ).is_err():
            self._use_error(err)
            return

        os.remove('___.tc')


    def __exists(self) -> Result[None, CreatorManagerError]:
        for token in self.basic:
            if not (token in self._data):
                return Err(error=CreatorManagerError(
                    message=f'Invalid metadata content | {token} not in metadata',
                    filename=self.name,
                    line=45,
                ))

        return Ok()


    def get_content(self) -> Result[None, CreatorManagerError]:
        var: str = 'target'
        if not (var in self._data):
            return Err(error=CreatorManagerError(
                message='Content var not found',
                filename=self.name,
                line=58,
            ))

        name: str = self._data[var]
        data: Result = FileManager().read.as_list(name)
        if data.is_err():
            return data

        content: list = data.value

        self._data[var] = content
        return Ok()


