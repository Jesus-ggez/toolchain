#~>
from src.core.safe_cls import SafeClass
from src.core.result import (
    Result,
    Err,
    Ok,
)


#<·
class ContentCreator(SafeClass):
    def __init__(self, alias: str, data: str) -> None:
        super().__init__()

        self._value: dict = {}


    @property
    def value(self) -> dict:
        return self._value
