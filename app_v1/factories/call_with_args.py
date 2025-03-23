#~>
from .base_factory import TokenFactory
from utils.result import (
    Result,
    Err,
    Ok,
)


class CallWithArgsFactory(TokenFactory):
    def __init__(self, context: dict, token: str) -> None:
        super().__init__(context, token)


    ...

