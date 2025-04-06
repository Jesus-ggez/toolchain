#~>
from src.utils.base_safe import SafeClass
from src.core import FileManager
from .errors import StartError
from .data import data
from utils.result import (
    Result,
    Err,
)


class StartManager(SafeClass):
    def __init__(self, tempname: str) -> None:
        self.name: str = self.__class__.__name__
        super().__init__()

        # only read
        if tempname == '_':
            return

        if not tempname or not (tempname in data):
            self._use_error(Err(error=StartError(
                message='Invalid tempname',
                filename=self.name,
            )))
            return

        actor: FileManager = FileManager()

        content: str = data[tempname]

        action: Result = actor.write.from_list(
            content=[content],
            name='___.tc',
        )
        if action.is_err():
            self._use_error(action)
            return
