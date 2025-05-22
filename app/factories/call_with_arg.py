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
class CallWithArgFactory(TokenFactory):
    tag: str = '::'

    def __init__(self, context: dict, token: str) -> None:
        super().__init__(context, token)

        self.__build()


    def __build(self) -> None:
        if not self._is_handler():
            return self._use_handler(instance=CallWithArgFactory)

        if ( err := self.__call() ).is_err():
            return self._use_error(err)


    def __call(self) -> Result[None, FactoryError]:
        if not callable(self._context['node_pointer']):
            return Err(error=FactoryError(
                message='This node are not a function:\t' + self._token,
                call='CallWithArgFactory.__call',
                source=__name__,
            ))

        if ( err := self.__wrap_exec_func() ).is_err():
            return Err(error=FactoryError(
                message=f'The function has failed, it says: \n\n{err.error}',
                call='CallWithArgFactory.__call <-> .__wrap',
                source=__name__,
            ))

        return Ok()


    def __wrap_exec_func(self) -> Result[None, Exception]:
        try:
            self._context['node_pointer'](self._token)
            return Ok()

        except Exception as e:
            return Err(error=e)
