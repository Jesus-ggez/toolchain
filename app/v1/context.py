#~>
from .token_factory import ActionsFactory, TokenFactory
from .errors import ContextError, TokenError
from src.core.safe_cls import SafeClass
from utils.result import (
    Result,
    Err,
    Ok,
)


class ContextManager(SafeClass):
    def __init__(self, context: dict, token: str) -> None:
        self._error: Result = Ok()

        constructor: Result = self.constructor(context=context, token=token)
        if constructor.is_err():
            self._use_error(constructor)
            return

        # handler: None | TokenFactory ['.']
        if self._context['handler']:
            action: TokenFactory = self._context['handler'](
                self._context,
                self._token,
            )
            if ( err := action.check_error() ).is_err():
                self._use_error(err)

            return

        # handler == None
        handler: Result = ActionsFactory.get_factory(name=self._token)
        if handler.is_err():
            self._use_error(handler)
            return

        # handler::None -> TokenFactory
        action: TokenFactory = handler.value(
            context=self._context,
            token=self._token,
        )
        if action.check_error().is_err():
            self._use_error(action.check_error())

        return


    def constructor(self, context: dict, token: str) -> Result[None, ContextError]:
        if not context:
            return Err(error=ContextError(
                call='ContextManager.constructor',
                message='Context is empty',
                source=__name__,
            ))

        if not token:
            return Err(error=TokenError(
                call='ContextManager.constructor',
                message='Invalid Token',
                source=__name__,
                token=token,
            ))

        self._context: dict = context
        self._token: str = token

        return Ok()
