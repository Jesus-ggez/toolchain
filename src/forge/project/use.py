#~>
from src.utils.base_safe import SafeClass
from utils.result import (
    Result,
    Err,
    Ok,
)


class UseProject(SafeClass):
    def __init__(self, identifier: str, alias: str) -> None:
        super().__init__()
