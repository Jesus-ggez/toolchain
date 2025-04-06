#~>
from src.forge.project.templates.blank import blank
from src.core import FileManager
from .model import Factory
from utils.result import (
    Result,
    Ok,
)


class Blank(Factory):
    def __init__(self) -> None:
        super().__init__()
        self._use_tag('_')


    def build(self) -> Result[None, Exception]:
        action: Result = FileManager().write.from_str(
            name='___.tc',
            content=blank,
        )

        if action.is_err():
            return action

        return Ok()
