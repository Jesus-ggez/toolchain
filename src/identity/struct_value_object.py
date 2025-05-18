from typing import Any, NamedTuple


#~>
from src.core.safe_cls import SafeClass


#<·
class VOIdentity(SafeClass):
    def __init__(self) -> None:
        super().__init__()
        self._model: Any = None
        self._value: Any = None


    def _create_value_object(self, **kwargs) -> None:
        self._value = self._model(**kwargs)


    @property
    def value(self) -> NamedTuple:
        return self._value
