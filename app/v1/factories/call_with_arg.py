#~>
from .base_factory import TokenFactory
from .errors import FactoryError
from utils.result import (
    Result,
    Err,
    Ok,
)


class CallWithArgFactory(TokenFactory):
    tag: str = '::'
    def __init__(self, context: dict, token: str) -> None:
        self.name: str = self.__class__.__name__
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
                message=f'This node are not a function:\t' + self._token,
                call='CallWithArgFactory.__call',
                source=__name__,
            ))

        call: Result = self.__wrap()
        if call.is_err():
            return Err(error=FactoryError(
                message=f'The function has failed, it says:\n\n{call.error}',
                call='CallWithArgFactory.__call <-> __wrap',
                source=__name__,
            ))

        return Ok()

    def __wrap(self) -> Result[None, Exception]:
        try:
            self._context['node_pointer'](self._token)
            return Ok()

        except Exception as e:
            return Err(e)

