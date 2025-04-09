#~>
from src.utils.base_safe import SafeClass
from .errors import FactoryError
from utils.result import (
    Result,
    Err,
    Ok,
)


class Factory(SafeClass):
    def __init__(self, content: list[str]) -> None:
        self._content: list[str] = content
        super().__init__()


    def _use_tag(self, name: str) -> None:
        self._name: str = name


    def build(self) -> Result[str, Exception]:
        for value in self._content:
            line: str = value.strip()

            if not line.startswith(self._name):
                continue

            new: list[str] = line.removeprefix(self._name).split('=')
            if len(new) != 2:
                return Err(error=FactoryError(
                    message='Invalid syntax',
                    call=self._name.upper() + 'Factory.build',
                    source=__name__,
                ))

            final: str = new[1].replace('"', '')
            return Ok(final)


        return Err(error=FactoryError(
            message=f'Token not found: {self._name}',
            call=self._name.upper() + 'Factory.build',
            source=__name__,
        ))
