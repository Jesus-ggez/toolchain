#~>
from .result import (
    Result,
    Ok,
)


#<·
class SafeClass:
    def __init__(self) -> None:
        self._tc_repr: str = 'Coordinator'
        self._state: Result = Ok()


    def _use_error(self, e: Result) -> None:
        self._state: Result = e


    def check_error(self) -> Result[None, Exception]:
        return self._state


    def __repr__(self) -> str:
        return self._tc_repr


    def __str__(self) -> str:
        return self.__class__.__name__ + 'is an class type: ' + self._tc_repr
