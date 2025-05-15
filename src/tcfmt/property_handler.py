from typing import Any


#~>
from src.core.safe_cls import SafeClass
from src.core.result import (
    Result,
    Err,
    Ok
)


#.?
from .parsers.errs import ParserError
from .parsers.data import parsers
from .errs import PropertyError


#<·
class PropertyHandler(SafeClass):
    def __init__(self, p: str, custom_filter: str) -> None:
        super().__init__()

        self._custom_filter: str = custom_filter
        self._prop: str = p

        self.__build()


    def __build(self) -> None:
        instructions: tuple = (
            self.__validate_parameters,
            self.__validate_property,
            self.__validate_raw_format,
            self.__validate_raw_payload,
            self.__validate_payload_type,
            self.__create_payload,
        )

        for instruction in instructions:
            if ( err := instruction() ).is_err():
                return self._use_error(err)


    def __create_error(self, msg: str) -> Result[None, PropertyError]:
        return Err(error=PropertyError(
            call='PropertyHandler()',
            source=__name__,
            message=msg,
        ))


    def __validate_parameters(self) -> Result[None, PropertyError]:
        if not self._prop.strip() or not self._custom_filter.strip():
            return self.__create_error(msg='Property not found')
        return Ok()


    def __validate_property(self) -> Result[None, PropertyError]:
        if self._prop.startswith(self._custom_filter):
            return Ok()

        return self.__create_error(msg='Invalid Property')


    def __validate_raw_format(self) -> Result[None, PropertyError]:
        self._parts: list[str] = self._prop.removeprefix(
            self._custom_filter,
        ).split('=')

        if self._parts != 2:
            return self.__create_error(msg='Invalid format property')
        return Ok()


    def __validate_raw_payload(self) -> Result[None, PropertyError]:
        if not self._parts[1].strip():
            return self.__create_error(msg=f'Invalid payload from {self._prop}')

        self._raw_payload: str = self._parts[1]
        return Ok()


    def __validate_payload_type(self) -> Result[None, PropertyError]:
        if not (self._raw_payload[0] in parsers):
            return self.__create_error(msg='Invalid format to use payload')

        return Ok()


    def __create_payload(self) -> Result[None, ParserError]:
        action: Result = parsers[self._raw_payload[0]](self._raw_payload)

        if action.is_ok():
            self.__value = action.value
            return Ok()

        return action


    @property
    def value(self) -> Any:
        return self.__value
