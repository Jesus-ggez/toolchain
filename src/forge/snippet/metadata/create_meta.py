#~>
from .errors import SnippetMetadataError
from .base_meta import BaseMeta
from utils.result import (
    Result,
    Err,
    Ok,
)
from .meta_statistics import MetaStatistics
from .analyzer_code import MetaAnalyzerCode
from .analysis import MetaAnalysis
from .meta_name import MetaName
from .meta_lang import MetaLang


class CreateMeta(BaseMeta):
    def __init__(self, content: list) -> None:
        super().__init__()
        self.name: str = self.__class__.__name__

        action: Result = self.filter(content)
        if action.is_err():
            self._use_error(action)
            return


    def filter(self, data: list) -> Result[None, Exception]:
        if len(data) == 0:
            return Err(error=SnippetMetadataError(
                message='Document is empty',
                filename=self.name,
                line=34
            ))

        filters: tuple = (
            MetaAnalyzerCode,
            MetaStatistics,
            MetaAnalysis,
            MetaName,
            MetaLang,
        )
        for filt in filters:
            action = filt(data)
            if action.check_error().is_err():
                return action

        return Ok()

