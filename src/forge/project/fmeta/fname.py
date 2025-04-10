#~>
from .model import FactoryMeta


class NameFactoryMeta(FactoryMeta):
    def __init__(self) -> None:
        super().__init__()

        self._use_tag('name')
