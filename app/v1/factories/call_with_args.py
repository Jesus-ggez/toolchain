#~>
from .base_factory import TokenFactory
from .errors import FactoryError
from utils.result import (
    Result,
    Err,
    Ok,
)


class CallWithArgsFactory(TokenFactory):
    tag: str = '·'
    def __init__(self, context: dict, token: str) -> None:
        self.name: str = self.__class__.__name__
        super().__init__(context, token)
        separator: str = ','

        if self._token == separator:
            return

        if not self._is_handler():
            self._use_handler(instance=CallWithArgsFactory)
            return

        if not self.__is_keyword():
            self.__add_argument()
            return

        action: Result = self.__call()
        if action.is_err():
            self._use_error(action)


    def __add_argument(self) -> None:
        self._context['args'].append(self._token)


    def __is_keyword(self) -> bool:
        return self._token == self.tag


    def __call(self) -> Result[None, FactoryError]:
        if not callable(self._context['node_pointer']):
            return Err(error=FactoryError(
                message=f'This node are not a function:\t' + self._token,
                call='CallWithArgsFactory.__call',
                source=__name__,
            ))

        call: Result = self.__wrap()
        if call.is_err():
            return Err(error=FactoryError(
                message=f'The function has failed, it says:\n\n{call.error}',
                call='CallWithArgsFactory.__call <-> __wrap',
                source=__name__,
            ))

        return Ok()


    def __wrap(self) -> Result[None, Exception]:
        try:
            self._context['node_pointer'](*self._context['args'])
            return Ok()

        except Exception as e:
            return Err(e)

