#~>
from src.core.safe_cls import SafeClass
from src.core.result import (
    Result,
    Err,
    Ok,
)


#<·
class TestCase(SafeClass):
    def __init__(
        self,
        *,
        fn,
        type_params: int
    ) -> None:
        super().__init__()
