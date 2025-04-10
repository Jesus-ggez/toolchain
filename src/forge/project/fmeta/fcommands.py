#~>
from .model import FactoryMetaList


class CommandsFactoryMeta(FactoryMetaList):
    def __init__(self) -> None:
        super().__init__()

        self._use_tag('commands')
