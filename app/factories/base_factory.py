#~>
from src.core.safe_cls import SafeClass
from src.core.result import Result, Ok


#<·
class TokenFactory(SafeClass):
    def __init__(self, context: dict, token: str) -> None:
        super().__init__()
        self._error: Result = Ok()
        self._context: dict = context
        self._token: str = token


    def _is_handler(self) -> bool:
        return self._context['handler'] != None


    def _use_handler(self, instance: type) -> None:
        self._context['handler'] = instance

