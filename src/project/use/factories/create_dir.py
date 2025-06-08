from typing import Any
import os


#~>
from src.core.safe_cls import SafeClass
from src.core.errors import safe_exec


#<·
class CreateDir(SafeClass):
    def __init__(self, context: dict) -> None:
        super().__init__()

        self._context: dict = context
        self.__build()


    def __build(self) -> None:
        # return print('creando carpeta')

        if ( err := self.__create_dir() ).is_err():
            return self._use_error(err)


    @safe_exec
    def __create_dir(self) -> Any:
        return os.mkdir(
            self._context['last_token']
        )
