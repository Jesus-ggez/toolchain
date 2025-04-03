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
        self._type('simple')


    def build(self, content) -> Result[None, Exception]:
        _content = content.content

        print(content, type(content))

        action: Result = FileManager().write.from_str(
            name=content.name,
            content=_content,
        )

        if action.is_err():
            return action

        return Ok()
