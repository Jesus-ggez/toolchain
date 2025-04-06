#~> Other tree for this
from src.core import FileManager
from .base import Factory
from utils.result import (
    Result,
    Err,
    Ok,
)


class Generator(Factory):
    def __init__(self) -> None:
        super().__init__()
        self._use_type('gen')


    def build(self, content: type) -> Result[None, Exception]:
        if ( err := self.create_metadata(content=content) ).is_err():
            return err

        ...


