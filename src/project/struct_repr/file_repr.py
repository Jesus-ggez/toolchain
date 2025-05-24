#~>
from src.core.safe_cls import SafeClass
from src.core.result import (
    Result,
    Ok,
)


#.?
from .errs import RepresentationError


#<·
class CreatorFilesRepr(SafeClass):
    def __init__(self, items: list) -> None:
        super().__init__()

        self._items: list = items
        self._value: str = ''

        self.__build()


    def __build(self) -> None:
        if not self._items:
            return

        for check in (
            self.__create_from_elements,
        ):
            if ( err := check() ).is_err():
                return self._use_error(err)


    def __create_from_elements(self) -> Result[None, RepresentationError]:
        comma: str = ','

        items: str = ','.join(self._items).strip()

        items.removeprefix(comma).removesuffix(comma)

        self._value = f'[{items}]'

        return Ok()


    @property
    def value(self) -> str:
        return self._value
