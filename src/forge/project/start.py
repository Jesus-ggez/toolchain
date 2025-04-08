#~>
from src.utils.base_safe import SafeClass
from src.utils.const import Constants
from .errors import StartProjectError
from src.core import FileManager
from .fstart.data import data
from utils.result import (
    Result,
    Err,
    Ok,
)


class StartProject(SafeClass):
    def __init__(self, name: str) -> None:
        super().__init__()

        if not name:
            self._use_error(Err(error=StartProjectError(
                message='Must',
                call='StartProject()',
                source=__name__,
            )))

        self._name: str = name


    def build(self) -> Result[None, StartProjectError]:
        if not (self._name in data):
            return Err(error=StartProjectError(
                message='Invalid template name',
                call='StartProject.build',
                source=__name__,
            ))

        action: Result = FileManager().write.from_str(
            name=Constants.START,
            content=data[self._name]
        )
        if action.is_err():
            return action

        return Ok()
