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
        self._final_content: dict = {}
        self._filters: list = []


    def build(self) -> None:
        if ( err := self._read_file() ).is_err():
            return self._use_error(err)

        if ( err := self._read_data() ).is_err():
            return self._use_error(err)


    def _read_file(self) -> Result[None, TcErr]:
        file: Result = Reader.as_list(TcConfig.FILE_NAME)
        if file.is_err():
            return file

        self._file_content.extend(file.value[1:])
        return Ok()


    def _read_data(self) -> Result[None, TcFmtError]:
        for line in self._file_content:
            if ( err := self._use_filters(item=line) ).is_err():
                return err

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
        if not self._filters:
            return Ok()

        for filt in self._filters.copy():
            if ( val := get_property(item=item, name=filt) ).is_ok():
                self._filters.remove(filt)
                self._final_content.update( { filt: val.value } )
                return Ok()

        return Err(error=TcFmtError(
            message=f'Missing property for this document {item}',
            call='TcFileReader._use_filters',
            source=__name__,
        ))


    @property
    def final_content(self) -> dict:
        return self._final_content


class TcFileCreator(SafeClass):
    def __init__(self, root: str) -> None:
        super().__init__()
        if not root:
            return self._use_error(Err(error=TcErr(
                message='Invalid tree name',
                call='TcFileCreator()',
                source=__name__,
            )))

        self._data_templates: dict = data_templates[root]


    def create_document(self, tempname: str) -> None:
        if not tempname:
            return self._use_error(Err(error=TcFmtError(
                call='TcFileCreator.create_document',
                message='Invalid template name',
                source=__name__,
            )))

        if not (tempname in self._data_templates):
            return self._use_error(Err(error=TcFmtError(
                call='TcFileCreator.create_document',
                message='Invalid template name',
                source=__name__,
            )))

        if ( err := Writer.from_str(
            content=self._data_templates[tempname],
            name=TcConfig.FILE_NAME,
        ) ).is_err():
            return self._use_error(err)
