#~>
from src.core.safe_cls import SafeClass
from src.core.result import (
    Result,
    Ok,
)


#.?
from .errs import TcProjectSyntaxError


#<·
class IncrementFileStack(SafeClass):
    def __init__(self, context: dict) -> None:
        super().__init__()

        self._context: dict = context
        self.__build()


    def __build(self) -> None:
        # return print('agregando al stack')

        if ( err := self.__increment_stack() ).is_err():
            return self._use_error(err)


    def __increment_stack(self) -> Result[None, TcProjectSyntaxError]:
        self._context['stack'].append(
            self._context['last_token']
        )

        return Ok()
