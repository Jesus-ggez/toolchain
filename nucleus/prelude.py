from typing import Any


#~>
from src.core.result import Result


#.?
from .constants import TcConfig


#<·
class TcLog:
    def __init__(self, v: Any) -> None:
        if not TcConfig['details']: return

        self._value: Any = v

        self.__build()


    def __build(self) -> None:
        if self.__use_error_repr():
            return

        self.__to_lang_types()

        if self.__use_not_null():
            return

        print(self._value)


    def __to_lang_types(self) -> None:
        if isinstance(self._value, Result):
            self._value = self._value.value


    def __use_not_null(self) -> bool:
        if not TcConfig['not-null']:
            return False

        if isinstance(self._value, str) and self._value.strip() == '':
            return True

        if self._value is None:
            return True

        return False


    def __use_error_repr(self) -> bool:
        if not TcConfig['errs']:
            return False

        if not isinstance(self._value, Result):
            return False

        if self._value.is_ok():
            return False

        print(str(self._value))
        return True
