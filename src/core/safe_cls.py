#~>
from .result import (
    Result,
    Ok,
)


class SafeClass:
    def __init__(self) -> None:
        self._state: Result = Ok()


    def _use_error(self, e: Result) -> None:
        self._state: Result = e


    def check_error(self) -> Result[None, Exception]:
        return self._state
