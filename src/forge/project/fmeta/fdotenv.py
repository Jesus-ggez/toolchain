#~>
from .model import Factory


class DotEnvFactory(Factory):
    def __init__(self, content: list[str]) -> None:
        super().__init__(content)

        self._use_tag('env')
        self.build()
