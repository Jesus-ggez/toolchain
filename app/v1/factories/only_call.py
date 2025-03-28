#~>
from .base_factory import TokenFactory
from utils.errors import safe_exec
from .errors import FactoryError
from utils.result import (
    Result,
    Err,
    Ok,
)


class OnlyCallFactory(TokenFactory):
    tag: str = '.'
    def __init__(self, context: dict, token: str) -> None:
        self.name: str = self.__class__.__name__
        super().__init__(context, token)

        """
        if not self._is_handler():
            self._use_handler(instance=OnlyCallFactory)
            return

        """
        action: Result = self.__call()
        if action.is_err():
            self._use_error(action)


    def __call(self) -> Result[None, FactoryError]:
        if not callable(self._context['node_pointer']):
            return Err(error=FactoryError(
                message=f'This node are not a function: ' + self._token,
                filename=self.name,
                line=30,
            ))

        call: Result = self.__wrap()
        if call.is_err():
            return Err(error=FactoryError(
                message=f'The function has failed, it says: {call}',
                filename=self.name,
                line=38,
            ))

        return Ok()

    def __wrap(self) -> Result[None, FactoryError]:
        try:
            self._context['node_pointer']()
            return Ok()

        except Exception as e:
            return Err(error=FactoryError(
                message=f'Error in exec: {e}',
                filename=self.name,
                line=49,
            ))
