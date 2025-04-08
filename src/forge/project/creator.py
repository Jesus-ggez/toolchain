#~>
from src.utils.base_safe import SafeClass
from src.utils.const import Constants
from src.core import FileManager
from utils.result import (
    Result,
    Err,
    Ok,
)


class CreatorManager(SafeClass):
    def __init__(self) -> None:
        super().__init__()


    def build(self) -> Result[None, Exception]:
        document: Result = FileManager().read.as_list(
            name=Constants.START,
        )
        return Ok()
