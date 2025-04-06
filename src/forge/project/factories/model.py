#~>
from src.utils.base_safe import SafeClass
from utils.result import (
    Result,
    Err,
    Ok,
)


class Factory(SafeClass):
    def _use_tag(self, tag: str) -> None:
        self.tag: str = tag


    def build(self) -> Result[None, Exception]:
        ...
