#~>
from .model import FactoryMeta


class BeginFactoryMeta(FactoryMeta):
    def __init__(self) -> None:
        super().__init__()

        self._use_tag('begin')
