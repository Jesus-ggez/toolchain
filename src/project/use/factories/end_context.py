from typing import Any
import os


#~>
from src.core.safe_cls import SafeClass
from src.core.errors import safe_exec
from src.core.result import (
    Result,
    Ok,
)


#.?
from .create_files_from_stack import CreateFilesFromStack
from .errs import TcErr


#<·
class EndContext(SafeClass):
    def __init__(self, context: dict) -> None:
        super().__init__()

        self._context: dict = context
        self.__build()


    def __build(self) -> None:
        # return print('saliendo de la carpeta')

        if ( err := self.__verify_node() ).is_err():
            return self._use_error(err)

        if ( err := self.__out_to_dir() ).is_err():
            return self._use_error(err)


    def __verify_node(self) -> Result[None, TcErr]:
        if self._context['stack']:
            action: CreateFilesFromStack = CreateFilesFromStack(context=self._context)

            if ( err := action.check_error() ).is_err():
                return err

        return Ok()

    @safe_exec
    def __out_to_dir(self) -> Any:
        return os.chdir('..')

