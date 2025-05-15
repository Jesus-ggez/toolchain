#~>
from src.core.safe_cls import SafeClass
from src.core.result import (
    Result,
    Err,
    Ok,
)


#.?
from .factories.base_factory import TokenFactory
from .token_factory import ActionsFactory
from .errs import ContextError


#<·
class ContextManager(SafeClass):
    def __init__(self, context: dict, token: str) -> None:
        super().__init__()

        self._context: dict = context
        self._token: str = token

        self.__build()


    def __build(self) -> None:
        if ( err := self.__validate_parameters() ).is_err():
            return self._use_error(err)

        if self._context.get('handler') is None:
            return self._use_error(self.__create_handler())

        if ( err := self.__use_handler() ).is_err():
            return self._use_error(err)


    def __create_error(self, msg: str) -> Result[None, ContextError]:
        return Err(error=ContextError(
            call='ContextManager',
            source=__name__,
            message=msg,
        ))


    def __validate_parameters(self) -> Result[None, ContextError]:
        if not self._context or not self._token:
            return self.__create_error(msg='Invalid context or token')

        return Ok()


    def __use_handler(self) -> Result[None, Exception]:
        action: TokenFactory = self._context['handler'](
            self._context,
            self._token,
        )

        return action.check_error()


    def __create_handler(self) -> Result[None, Exception]:
        get_handler: Result = ActionsFactory.get_factory(
            name=self._token,
        ) # return error if not exists factory
        if get_handler.is_err(): return get_handler


        set_action: Result = get_handler.value(
            context=self._context,
            token=self._token,
        ).check_error() # direct to result

        if ( err := set_action ).is_err():
            return err

        return Ok()
