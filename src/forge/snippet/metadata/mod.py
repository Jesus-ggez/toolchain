#~>
from .errors import SnippetMetadataError
from .create_meta import CreateMeta
from src.core import FileManager
from .base_meta import BaseMeta
from utils.result import (
    Result,
    Err,
    Ok,
)


class SnippetMetadata(BaseMeta):
    def __init__(self, context: dict) -> None:
        super().__init__()

        self.name: str = self.__class__.__name__
        if not context:
            self._use_error(Err(error=SnippetMetadataError(
                message='Context necessary for this action',
                filename=self.name,
                line=12,
            )))

    def generate(self) -> Result[None, Exception]:
        base: FileManager = FileManager()

        _document: Result = base.read.as_list('___.tc')
        if _document.is_err():
            return _document # error

        document: list = _document.data

        action: CreateMeta = CreateMeta(content=document)
        if action.check_error().is_err():
            return action.check_error()

        return Ok()


