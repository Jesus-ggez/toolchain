#~>
from .errors import TcErr
from .result import (
    Result,
    Ok,
)


#<·
class SafeClass:
    def __init__(self) -> None:
        self._state: Result = Ok()


    def _use_error(self, e: Result) -> None:
        self._state: Result = e


    def check_error(self) -> Result[None, TcErr]:
        from nucleus.prelude import TcLog

        TcLog(v=self._state)

        return self._state
