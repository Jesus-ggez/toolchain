#~>
from src.utils.base_safe import SafeClass
from .errors import FactoryError
from utils.result import (
    Result,
    Err,
    Ok,
)


class Factory(SafeClass):
    def __init__(self, raw: dict) -> None:
        self.name: str = self.__class__.__name__
        self.constructor(raw=raw)
        super().__init__()


    def constructor(self, raw: dict) -> None:
        if not raw['file']:
            self._use_error(Err(error=FactoryError(
                message='Context not found',
                filename=self.name,
                line=0,
            )))

        if not ('file' in raw):
            self._use_error(Err(error=FactoryError(
                message='File content not found',
                filename=self.name,
                line=0,
            )))

        self._raw: dict = raw


    def build(self, token: str) -> Result[list, FactoryError]:
        for item in self._raw['file']:
            if item.startswith(token):
                return Ok(item.split())

        return Err(error=FactoryError(
            message='Token not found',
            filename=self.name,
            line=0
        ))
