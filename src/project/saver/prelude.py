#~>
from src.core.safe_cls import SafeClass
from src.core.result import (
    Result,
    Err,
    Ok,
)


#<·
class ProjectSaver(SafeClass):
    def __init__(self, metadata: dict) -> None:
        super().__init__()


    @property
    def value(self) -> str:
        ...

