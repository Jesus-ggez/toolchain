#~>
from src.utils.base_safe import SafeClass


class SnippetMainHandler(SafeClass):
    def __init__(self, identifier: str) -> None:
        super().__init__()

