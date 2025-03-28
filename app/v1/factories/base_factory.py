#~>
from src.utils.base_safe import SafeClass
from utils.result import Result, Ok


class TokenFactory(SafeClass):
    def __init__(self, context: dict, token: str) -> None:
        self._error: Result = Ok()
        self._context: dict = context
        self._token: str = token
        #print(self.__class__.__name__)


    def _is_handler(self) -> bool:
        return self._context['handler'] != None


    def _use_handler(self, instance: type) -> None:
        self._context['handler'] = instance
        #print(self.__class__.__name__, self._context)
