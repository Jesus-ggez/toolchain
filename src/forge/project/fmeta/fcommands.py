#~>
from .model import Factory


class CommandsFactory(Factory):
    def __init__(self, content: list[str]) -> None:
        super().__init__(content)

        self._use_tag('commands')
        self.build()
