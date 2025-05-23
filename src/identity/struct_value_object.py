from typing import Any, Callable


#~>
from src.core.safe_cls import SafeClass
from src.core.result import Err


#.?
from .errs import ValueObjectCreationError


#<·
class VOIdentity(SafeClass):
    def __init__(self) -> None:
        super().__init__()
        self._model: Callable = Any
        self._value: Any = None


    def _create_value_object(self, **kwargs) -> None:
        if self._model is None:
            return self._use_error(Err(error=ValueObjectCreationError(
                call='_create_value_object()',
                message='Invalid creation',
                source=__name__,
            )))

        self._value = self._model(**kwargs)


    @property
    def value(self) -> Any:
        return self._value
