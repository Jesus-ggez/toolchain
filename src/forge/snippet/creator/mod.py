import os


#~>
from src.utils.base_safe import SafeClass
from .errors import CreatorManagerError
from src.utils.const import Constants
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

        os.remove(Constants.START)


    def __exists(self) -> Result[None, CreatorManagerError]:
        for token in self.basic:
            if not (token in self._data):
                return Err(error=CreatorManagerError(
                    message=f'Invalid metadata content | {token} not in metadata',
                    call='CreatorManager.__exists',
                    source=__name__,
                ))

        return Ok()


    def get_content(self) -> Result[None, CreatorManagerError]:
        var: str = 'target'
        if not (var in self._data):
            return Err(error=CreatorManagerError(
                call='CreatorManager.get_content',
                message='Content var not found',
                source=__name__,
            ))

        name: str = self._data[var]
        data: Result = FileManager().read.as_list(name)
        if data.is_err():
            return data

        content: list = data.value

        self._data[var] = content
        return Ok()


