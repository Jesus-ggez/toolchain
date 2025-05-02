#~>
from src.core.file_utils import Reader, Writer
from src.tcfiles.data import data_templates
from src.core.safe_cls import SafeClass
from src.core.errors import TcErr
from src.core.result import (
    Result,
    Err,
    Ok,
)

#.?
from .property_handler import get_property
from .constants import TcConfig
from .errs import TcFmtError


#<·
class TcFileReader(SafeClass):
    def __init__(self) -> None:
        super().__init__()
        self._file_content: list[str] = []
        self._filters: list = []
        self._final_content: dict = {}

        begin: Result = self._read_file()
        if begin.is_err():
            self._use_error(begin)
            return

        mid: Result = self._read_data()
        if mid.is_err():
            self._use_error(mid)
            return


    def _read_file(self, ) -> Result[None, TcErr]:
        res: Result = Reader.as_list(TcConfig.FILE_NAME)
        if res.is_err():
            return res

        self._file_content.extend(res.value)
        return Ok()


    def _read_data(self) -> Result[None, TcFmtError]:
        for line in self._file_content:
            res: Result = self._use_filters(item=line)
            if res.is_err():
                return res

        return Ok()


    def add_filters(self, props: list[str]) -> Result[None, TcErr]:
        if not props: return Err(error=TcErr(
            message='this field must not be empty',
            call='TcFileReader.add_filters',
            source=__name__,
        ))

        self._filters.extend(props)
        return Ok()


    def _use_filters(self, item: str) -> Result[None, TcFmtError]:
        for filt in self._filters:
            data: Result = get_property(
                item=item,
                name=filt,
            )

            if data.is_ok():
                self._filters.remove(filt)
                self._final_content.update( { filt: data.value } )

                return Ok()

        return Err(error=TcFmtError(
            message='Missing property for this document',
            call='TcFileReader._use_filters',
            source=__name__,
        ))


    @property
    def final_content(self) -> dict:
        return self._final_content



class TcFileCreator(SafeClass):
    def __init__(self) -> None:
        super().__init__()


    def create_document(self, tempname: str) -> None:
        if not tempname:
            self._use_error(Err(error=TcFmtError(
                call='TcFileCreator.create_document',
                message='Invalid template name',
                source=__name__,
            ))); return

        if not (tempname in data_templates):
            self._use_error(Err(error=TcFmtError(
                call='TcFileCreator.create_document',
                message='Invalid template name',
                source=__name__,
            ))); return

        action: Result = Writer.from_str(
            content=data_templates[tempname],
            name=TcConfig.FILE_NAME,
        )

        if action.is_err():
            self._use_error(action)
            return
