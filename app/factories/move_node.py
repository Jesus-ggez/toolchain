#~>
from src.core.result import (
    Result,
    Err,
    Ok,
)


#.?
from .base_factory import TokenFactory
from .errs import FactoryError


#<·
class MoveNodeFactory(TokenFactory):
    tag: str = ':'

    def __init__(self, context: dict, token: str) -> None:
        super().__init__(context, token)

        if not self._is_handler():
            return self._use_handler(instance=MoveNodeFactory)

        if ( err := self.__move() ).is_err():
            return self._use_error(err)

        self.__reset_handler()


    def __reset_handler(self) -> None:
        self._context['handler'] = None


    def __move(self) -> Result[None, FactoryError]:
        current = self._context['node_pointer']

        if not isinstance(current, dict):
            return Err(error=FactoryError(
                message='Impossible move to other node',
                call='MoveNodeFactory.__move',
                source=__name__,
            ))

        if not (self._token in current):
            return Err(error=FactoryError(
                message='Node not found:\t' + self._token,
                call='MoveNodeFactory.__move',
                source=__name__,
            ))

        self._context['node_pointer'] = current[self._token]
        return Ok()

