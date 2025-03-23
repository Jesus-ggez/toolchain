#~>
from utils.result import Result, Ok
from .errors import FactoryError


class TokenFactory:
    def __init__(self, context: dict, token: str) -> None:
        self._error: Result = Ok()
        self._context: dict = context
        self._token: str = token

        print(f'Ok | {self.__class__.__name__}')


    def check_error(self) -> Result[None, FactoryError]:
        return self._error


    def _use_error(self, v: Result) -> None:
        self._error: Result = v


