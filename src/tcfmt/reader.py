#~>
from src.core.errs import FileReaderError
from src.core.safe_cls import SafeClass
from src.core.file_utils import Reader
from src.core.result import (
    Result,
    Err,
    Ok,
)


#.?
from .property_handler import PropertyHandler
from .errs import TcTcfmtReaderError
from .constants import TcConfig


#<·
class TcFileReader(SafeClass):
    def __init__(self) -> None:
        super().__init__()
        self._file_content: list[str] = []
        self._final_content: dict = {}
        self._filters: list[str] = []


    # necesary external call
    def build(self) -> None:
        for check in (
            self._read_file,
            self._read_data,
        ):
            if ( err := check() ).is_err():
                return self._use_error(err)


    def __create_error(self, msg: str) -> Result[None, TcTcfmtReaderError]:
        return Err(error=TcTcfmtReaderError(
            call='TcFileReader()',
            source=__name__,
            message=msg,
        ))


    def _read_file(self) -> Result[None, FileReaderError]:
        file: Result = Reader.as_list(TcConfig.FILE_NAME)

        if file.is_ok():
            self._file_content.extend(file.value[1:])

        return file


    def _read_data(self) -> Result[None, TcTcfmtReaderError]:
        for line in self._file_content:
            if line.startswith('#'):
                continue

            if not line.strip():
                continue

            if ( err := self._use_filters(item=line) ).is_err():
                return err

        return Ok()


    def add_filters(self, props: list[str]) -> Result[None, TcTcfmtReaderError]:
        if not props:
            return self.__create_error(msg='This field must be empty')

        self._filters.extend(props)
        return Ok()


    def _use_filters(self, item: str) -> Result[None, TcTcfmtReaderError]:
        if not self._filters:
            return Ok()

        for filt in self._filters.copy():
            content: PropertyHandler = PropertyHandler(p=item, custom_filter=filt)
            if content.check_error().is_ok():
                self._filters.remove(filt)

                self._final_content.update( { filt: content.value } )
                return Ok()

        return self.__create_error(msg=f'Missing property for this document: {item}')


    @property
    def final_content(self) -> dict:
        return self._final_content
