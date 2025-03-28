#~>
from src.utils.base_safe import SafeClass


class MetadataManager(SafeClass):
    def __init__(self, context: dict) -> None:
        super().__init__()
