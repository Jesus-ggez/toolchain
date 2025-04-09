#~>
from .model import Factory


class _TypeFactory(Factory):
    def __init__(self, content: list[str]) -> None:
        super().__init__(content)

        self._use_tag('_type')
        self.build()
