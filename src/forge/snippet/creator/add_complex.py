#~>
from src.utils.base_safe import SafeClass
from utils.result import (
    Result,
    Err,
    Ok,
)


class ComplexMetadata(SafeClass):
    def __init__(self) -> None:
        super().__init__()
        self._use_error(Exception(
            'Impl in future'
        ))
