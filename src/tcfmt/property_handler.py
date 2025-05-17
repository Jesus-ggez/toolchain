#~>
from src.core.safe_cls import SafeClass
from src.core.result import (
    Result,
    Err,
    Ok,
)


#.?
from .filters_prop.data import data
from .errs import PropertyError


#<·
class PropertyHandler(SafeClass):
    def __init__(self, p: str, custom_filter: str) -> None:
        super().__init__()

        self._p: str = p.strip()
        self._custom_filter: str = custom_filter.strip()

        self.__build()


    def __build(self) -> None:
        if ( err := self.__validate_parameters() ).is_err():
            return self._use_error(err)

        if ( err := self.__validate_property_name() ).is_err():
            return self._use_error(err)

        if ( err := self.__create_raw_payload() ).is_err():
            return self._use_error(err)

        if ( err := self.__create_valid_payload() ).is_err():
            return self._use_error(err)


    def __create_error(self, msg: str) -> Result[None, PropertyError]:
        return Err(error=PropertyError(
            call='PropertyHandler()',
            source=__name__,
            message=msg,
        ))


    def __validate_parameters(self) -> Result[None, PropertyError]:
        if not self._p or not self._custom_filter:
            return self.__create_error(msg='Invallid parameters')

        return Ok()


    def __validate_property_name(self) -> Result[None, PropertyError]:
        if not self._p.startswith(self._custom_filter):
            return self.__create_error(msg='Invalid property name')

        return Ok()


    def __create_raw_payload(self) -> Result[None, PropertyError]:
        _raw_payload: str = self._p.removeprefix(self._custom_filter).strip()

        if not _raw_payload.startswith('='):
            return self.__create_error(msg=f'Invalid syntax: {_raw_payload}')

        self._payload: str = _raw_payload.removeprefix('=').strip()
        return Ok()


    def __create_valid_payload(self) -> Result[None, PropertyError]:
        filt = data.get(self._payload[0])

        if filt is None:
            return self.__create_error(msg=f'Invalid format to create payload: {self._payload}')

        filt_value: Result = filt(self._payload)

        if filt_value.is_err():
            return filt_value

        self._value: list | str = filt_value.value

        return Ok()


    @property
    def value(self) -> str | list:
        return self._value
