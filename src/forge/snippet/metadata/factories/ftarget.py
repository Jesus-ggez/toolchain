#~>
from .replace_basic import BasicFactory


class TargetFactory(BasicFactory):
    def __init__(self, raw: dict) -> None:
        self.token_name: str = 'target'
        super().__init__(raw)
