#~>
from .errors import NewProjectError
from src.utils.base_safe import SafeClass
from utils.result import (
    Result,
    Err,
    Ok,
)


class NewProject(SafeClass):
    def __init__(self) -> None:
        super().__init__()


    def build(self) -> Result[None, NewProjectError]: ...
