#~>
from .model import Factory


class LangsFactory(Factory):
    def __init__(self, content: list[str]) -> None:
        super().__init__(content)

        self._use_tag('langs')
        self.build()
