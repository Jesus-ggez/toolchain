#~>
from src.project.use.tc_ast import TcAST
from src.core.safe_cls import SafeClass
from src.core.result import (
    Result,
    Ok,
)


#.?
from .errs import TcProjectSyntaxError


#<·
class IncrementFileStack(SafeClass):
    def __init__(self, context: type[TcAST]) -> None:
        super().__init__()

        self._context: type[TcAST] = context
        self.__build()


    def __build(self) -> None:
        # return print('agregando al stack')

        if ( err := self.__increment_stack() ).is_err():
            return self._use_error(err)


    def __increment_stack(self) -> Result[None, TcProjectSyntaxError]:
        self._context.file_stack.append(self._context.last_token)

        return Ok()
