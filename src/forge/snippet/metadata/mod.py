#~>
from src.utils.base_safe import SafeClass
from src.utils.const import Constants
from src.core import FileManager
from utils.result import Result
from .app import MetaFactory


class MetadataManager(SafeClass):
    def __init__(self) -> None:
        self._metadata: dict = {}

        super().__init__()
        # file
        _data: Result = FileManager().read.as_list('./' + Constants.START)

        if _data.is_err():
            print(_data)
            self._use_error(_data)
            return

        data: list[str] = _data.value

        # file content raw to read
        meta_creator: Result = MetaFactory.get_factory(
            token=data[0].strip(),
        )
        if meta_creator.is_err():
            self._use_error(meta_creator)
            return

        # i dont known
        self._metadata['file'] = data[1:]
        self._factories: list = meta_creator.value


    def create_meta(self) -> None:
        for meta in self._factories:
            meta(self._metadata)


    @property
    def data(self) -> dict:
        return self._metadata
