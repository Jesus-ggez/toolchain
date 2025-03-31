#~>
from .replace_basic import BasicFactory


class TypeFactory(BasicFactory):
    def __init__(self, raw: dict) -> None:
        self.token_name: str = '_type'
        super().__init__(raw)
