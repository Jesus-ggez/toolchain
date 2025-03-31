#~>
from .replace_basic import BasicFactory


class LangFactory(BasicFactory):
    def __init__(self, raw: dict) -> None:
        self.token_name: str = 'lang'
        super().__init__(raw)
