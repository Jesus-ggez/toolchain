#~>
from utils.result import Result, Ok


class SafeClass:
    def __init__(self) -> None:
        self._error: Result = Ok()


    def check_error(self) -> Result[None, Exception]:
        return self._error


    def _use_error(self, error: Result) -> None:
        self._error: Result = error
