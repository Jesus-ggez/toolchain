#~>
from .base_factory import TokenFactory
from .errors import FactoryError
from utils.result import (
    Result,
    Err,
    Ok,
)


class MoveNodeFactory(TokenFactory):
    tag: str = ':'
    def __init__(self, context: dict, token: str) -> None:
        self.name: str = self.__class__.__name__
        super().__init__(context, token)

        if not self._is_handler():
            self._use_handler(instance=MoveNodeFactory)
            return

        action: Result = self.__move()
        if action.is_err():
            self._use_error(action)
            return

        self._remove_handler()


    def _remove_handler(self) -> None:
        self._context['handler'] = None


    def __move(self) -> Result[None, FactoryError]:
        current = self._context['node_pointer']

        if type(current) != dict:
            return Err(error=FactoryError(
                message='Impossible move to other node',
                call='MoveNodeFactory.__move',
                source=__name__,
            ))

        if not (self._token in current):
            return Err(error=FactoryError(
                message='Node not found: ' + self._token,
                call='MoveNodeFactory.__move',
                source=__name__,
            ))

        self._context['node_pointer'] = current[self._token]

        return Ok()
