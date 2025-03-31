#~>
from .replace_basic import BasicFactory


class NameFactory(BasicFactory):
    def __init__(self, raw: dict) -> None:
        self.token_name: str = 'name'
        super().__init__(raw)
