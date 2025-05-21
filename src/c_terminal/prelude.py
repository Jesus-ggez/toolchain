#~>
from utils.terminal import get_copy_next_arg, get_next_arg
from src.core.safe_cls import SafeClass
from src.core.result import (
    Result,
    Err,
    Ok,
)


#.?
from .errs import TerminalError


#<·
class Terminal(SafeClass):
    def __init__(self, field: str) -> None:
        super().__init__()

        self._default: str = '_'
        self._divider: str = '-'
        self._field: str = field

        self.__build()


    def __build(self) -> None:
        if ( err := self.__validate_parameters() ).is_err():
            return self._use_error(err)

        if self.__is_argument_default().is_ok(): return

        for check in (
            self.__is_valid_argument,
            self.__is_valid_format,
            self.__is_valid_final_value,
        ):
            if ( err := check() ).is_err():
                return self._use_error(err)

        self.__value = self._parts[1]


    def __create_error(self, msg: str) -> Result[None, TerminalError]:
        return Err(error=TerminalError(
            call='Terminal()',
            source=__name__,
            message=msg,
        ))


    def __validate_parameters(self) -> Result[None, TerminalError]:
        if not isinstance(self._field, str) or not self._field:
            return self.__create_error(msg='Unknown field name')

        return Ok()


    def __is_argument_default(self) -> Result[None, Exception]:
        if get_copy_next_arg().is_err():
            self.__value = self._default
            return Ok()

        return Err(Exception())


    def __is_valid_argument(self) -> Result[None, TerminalError]:
        self.__value: str = get_next_arg().value

        if self.__value.startswith(self._field):
            return Ok()

        print(self._field, self.__value)

        return self.__create_error(msg='Invalid format to flag')


    def __is_valid_format(self) -> Result[None, TerminalError]:
        self._parts: list[str] = self.__value.removeprefix(
            self._field,
        ).split(sep=self._divider)

        if len(self._parts) != 2:
            return self.__create_error(msg='Invalid terminal value')

        return Ok()


    def __is_valid_final_value(self) -> Result[None, TerminalError]:
        final_value: str = self._parts[1]

        if not final_value:
            return self.__create_error(msg=f'Invalid value for {self._field}')

        return Ok()

    @property
    def value(self) -> str:
        return self.__value
