from typing import Any


#~>
from src.core.errors import safe_exec
from src.core.safe_cls import SafeClass
from src.core.result import (
    Result,
    Err,
    Ok,
)


#.?
from .errs import UIFieldError, TcErr


#<·

class UIField(SafeClass):
    def __init__(self, field: str, len_sep: int) -> None:
        super().__init__()
        self._len_sep: int = 0 + ( len_sep if isinstance(len_sep, int) and len_sep > 0 else 0 )

        self._field: str = field

        self.__build()

        self._title: str = f"{self._field:^self._len_sep}"
        self._separation: int = self._len_sep
        self._value: str = self._field


    @property
    def title(self) -> str:
        return self._title


    @property
    def value(self) -> str:
        return self._value

    @property
    def separation(self) -> int:
        return self._separation


    def __build(self) -> None:
        if not isinstance(self._field, str):
            return self._use_error(Err(error=UIFieldError(
                message='Invalid field type',
                call='UIField()',
                source=__name__,
            )))

        if not self._field:
            return self._use_error(Err(error=UIFieldError(
                message='Missing field',
                call='UIField()',
                source=__name__,
            )))

        return


class UI(SafeClass):
    def __init__(self, fields: list[UIField]) -> None:
        super().__init__()
        self._ui_repr: str = ''

        self._fields: list[UIField] = fields

        self.__build()


    def __build(self) -> None:
        for check in (
            self.__validate_parameters,
            self.__create_repr,
        ):
            if ( err := check() ).is_err():
                return self._use_error(err)


    def build(self, items: dict) -> None:
        if ( err := self.__add_items(items) ).is_err():
            return self._use_error(err)

        if ( err := self.___show_repr() ).is_err():
            return self._use_error(err)

    def __create_error(self, msg) -> Result[None, UIFieldError]:
        return Err(error=UIFieldError(
            source=__name__,
            message=msg,
            call='UI()',
        ))


    def __validate_parameters(self) -> Result[None, UIFieldError]:
        if not isinstance(self._fields, list):
            return self.__create_error(msg='Invalid type from fields: {type(self._fields)}')

        if [ i for i in self._fields if not isinstance(i, UIField) ]:
            return self.__create_error(msg='Invalid items ingresed')

        return Ok()


    def __create_repr(self) -> Result[None, UIFieldError] | Result[None, TcErr]:
        repr_: str = ''

        for field in self._fields:
            if ( err := field.check_error() ).is_err():
                return err

            repr_ += field.title

        self._ui_repr += repr_ + '\n'
        return Ok()


    def __add_items(self, items: dict) -> Result[None, UIFieldError]:
        for item in self._fields:
            if not item.value in items:
                return self.__create_error(msg='')

            ...


    @safe_exec
    def ___show_repr(self) -> Any:
        return print(self._ui_repr)


