#~>
from src.core import FileManager
from .base import Factory
from utils.result import (
    Result,
    Ok,
)


class Simple(Factory):
    def __init__(self) -> None:
        super().__init__()
        self._use_type('simple')


    def build(self, content: type) -> Result[None, Exception]:
        if ( err := self.create_metadata(content=content) ).is_err():
            return err

        action: Result = FileManager().write.from_str(
            name=content.name + '.' + self.metadata.get('lang', '.txt'),
            content=self.file_content,
        )
        if action.is_err():
            return action

        return Ok()
