#~>
from src.utils.base_safe import SafeClass
from .errors import FactoryError
from .utils import fmt_to_list
from utils.result import (
    Result,
    Err,
    Ok,
)


class FactoryMeta(SafeClass):
    def __init__(self) -> None:
        super().__init__()
        self._rules: list = []


    def _use_tag(self, tag: str) -> None:
        self._tag: str = tag


    def __err(self, message: str) -> FactoryError:
        return FactoryError (
            message=message,
            call=self._tag.upper() + 'Factory.build',
            source=__name__,
        )


    def build(self, content: str) -> Result[str, Exception]:
        return self._build(content=content)


    def _build(self, content: str) -> Result[str, Exception]:
        self._content: str = content

        if not self._content.startswith(self._tag):
            return Err(error=self.__err(
                message=f'Token not found: {self._tag}',
            ))

        raw: list[str] = self._content.removeprefix(self._tag).strip().split('=')
        if len(raw) != 2:
            return Err(error=self.__err(
                message='Invalid syntax',
            ))

        value: str = raw[1].replace('"', '')
        if not value:
            return Err(error=self.__err(
                message='Invalid content',
            ))

        if self._rules:
            for rule in self._rules:
                value = rule(value)

        return Ok(value.replace(' ', ''))


class FactoryMetaList(FactoryMeta):
    def __init__(self) -> None:
        super().__init__()
        self._rules.append(fmt_to_list)
