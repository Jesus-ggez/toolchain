#~>
from src.core.safe_cls import SafeClass
from src.core.result import (
    Result,
    Err,
    Ok,
)


#<·
class ProjectUseWorkspace(SafeClass):
    def __init__(self, identifier: str, alias: str) -> None:
        super().__init__()


    @property
    def workspace_info(self) -> str:
        ...
