#~>
from src.forge.project.templates.blank import blank
from src.utils.const import Constants
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
        document: Result = FileManager().write.from_str(
            name=Constants.START,
            content=blank,
        )
        if document.is_err():
            return document

        return Ok()
