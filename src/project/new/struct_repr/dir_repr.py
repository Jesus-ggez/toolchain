#~>
from src.core.safe_cls import SafeClass
from src.core.result import (
    Result,
    Ok,
)


#.?
from .errs import RepresentationError


#<·
class CreatorDirsRepr(SafeClass):
    def __init__(self, items: list) -> None:
        super().__init__()

        self._items: list = items
        self._value: str = '.'

        self.__build()


    def __build(self) -> None:
        if not self._items:
            return

        if ( err := self.__create_from_elements() ).is_err():
            return self._use_error(err)


    def __create_from_elements(self) -> Result[None, RepresentationError]:
        dot: str = '.'

        items: str = dot.join(self._items).strip()

        value: str = items.removeprefix(dot).removesuffix(dot)

        self._value = f'-{value}|'

        return Ok()


    @property
    def value(self) -> str:
        return self._value
