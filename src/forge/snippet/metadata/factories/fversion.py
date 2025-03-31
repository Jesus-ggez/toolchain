#~>
from .replace_basic import BasicFactory


class VersionFactory(BasicFactory):
    def __init__(self, raw: dict) -> None:
        self.token_name: str = 'version'
        super().__init__(raw)
