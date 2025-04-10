#~>
from .model import FactoryMeta


class _TypeFactoryMeta(FactoryMeta):
    def __init__(self) -> None:
        super().__init__()

        self._use_tag('_type')
