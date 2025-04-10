#~>
from .model import FactoryMetaList


class IgnoreFactoryMeta(FactoryMetaList):
    def __init__(self) -> None:
        super().__init__()

        self._use_tag('ignore')
