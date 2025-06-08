from typing import Any
import os


#~>
from src.project.use.tc_ast import TcAST
from src.core.safe_cls import SafeClass
from src.core.errors import safe_exec


#<·
class EndContext(SafeClass):
    def __init__(self, context: type[TcAST]) -> None:
        super().__init__()

        self._context: type[TcAST] = context
        self.__build()


    def __build(self) -> None:
        # return print('saliendo de la carpeta')

        if ( err := self.__out_to_dir() ).is_err():
            return self._use_error(err)


    @safe_exec
    def __out_to_dir(self) -> Any:
        return os.chdir('..')

