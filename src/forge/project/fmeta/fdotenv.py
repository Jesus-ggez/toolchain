#~>
from .model import FactoryMetaList


class DotEnvFactoryMeta(FactoryMetaList):
    def __init__(self) -> None:
        super().__init__()

        self._use_tag('env')
