#~>
from .base_factory import TokenFactory
from utils.errors import safe_exec
from .errors import FactoryError
from utils.result import (
    Result,
    Err,
    Ok,
)


class CallWithArgFactory(TokenFactory):
    tag: str = '::'
    def __init__(self, context: dict, token: str) -> None:
        super().__init__(context, token)

        if not self._is_handler():
            self._use_handler(instance=CallWithArgFactory)
            return

        action: Result = self.__call()
        if action.is_err():
            self._use_error(action)


    def __call(self) -> Result[None, FactoryError]:
        if not callable(self._context['node_pointer']):
            return Err(error=FactoryError(
                message=f'This node are not a function: ' + self._token,
                filename=self.__class__.__name__,
                line=27,
            ))

        call: Result = self.__wrap()
        if call.is_err():
            return Err(error=FactoryError(
                message=f'There was an error while calling: {call.error}',
                filename=self.__class__.__name__,
                line=35,
            ))

        return Ok()

    @safe_exec
    def __wrap(self):
        self._context['node_pointer'](self._token)


