#~>
from src.core.errors import BaseError

#<·
class ContextError(BaseError): ...

class TokenError(ContextError):
    def __init__(self, source: str, call: str, message: str, token: str) -> None:
        super().__init__(
            message=message + f' | token: {token}',
            source=source,
            call=call,
        )


class TreeError(ContextError):
    def __init__(self, source: str, call: str, message: str) -> None:
        super().__init__(source, call, message)
