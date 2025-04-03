#~>
from src.utils.base_safe import SafeClass
from .errors import FactoryError
from utils.result import (
    Result,
    Err,
    Ok,
)


class Factory(SafeClass):
    def __init__(self) -> None:
        super().__init__()


    def _type(self, v: str) -> None:
        self.type: str = v


    def build(self, content: type) -> Result[None, Exception]:
        return Err(error=FactoryError(
            message='Not implemented',
            filename='Factory',
            line=-1,
        ))
