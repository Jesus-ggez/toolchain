#~>
from src.utils.base_safe import SafeClass
from .errors import StartError
from src.forge.snippet.creator.app import SnippetCreator
from utils.result import (
    Result,
    Err,
)


class StartManager(SafeClass):
    def __init__(self, tempname: str) -> None:
        self.name: str = self.__class__.__name__
        super().__init__()

        if not tempname:
            self._use_error(Err(error=StartError(
                message='Invalid tempname',
                filename=self.name,
            )))
            return

        if tempname == '_':
            return
