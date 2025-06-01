#~>
from src.core.safe_cls import SafeClass
from src.core.result import (
    Result,
    Err,
    Ok,
)


#<·
class RecursiveCreator(SafeClass):
    def __init__(self, data: dict) -> None:
        super().__init__()
