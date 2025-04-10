#~>
from .model import FactoryMetaList


class EntryFactoryMeta(FactoryMetaList):
    def __init__(self) -> None:
        super().__init__()

        self._use_tag('entry')
