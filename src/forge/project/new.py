#~>
from src.core.file_actions import FileManager
from src.utils.base_safe import SafeClass
from .fmeta.errors import FactoryError
from src.utils.const import Constants
from .errors import NewProjectError
from .fmeta.data import data
from utils.result import (
    Result,
    Err,
    Ok,
)


class NewProject(SafeClass):
    def __init__(self) -> None:
        super().__init__()

        ctt: Result = FileManager().read.as_list(
            name=Constants.START,
        )
        if ctt.is_err():
            self._use_error(ctt)
            return

        self._content: list[str] = ctt.value


    def build(self) -> Result[None, NewProjectError]:
        data: dict = {}
        for item in self._content:
            action: Result = self.__use_metadata(item=item)
            if action.is_err():
                return action

            data.update(action.value)

        return Ok()


    def __use_metadata(self, item: str) -> Result[dict, FactoryError]:
        ...
