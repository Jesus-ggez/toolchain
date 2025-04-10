#~>
from src.core.file_actions import FileManager
from src.utils.base_safe import SafeClass
from .fmeta.errors import FactoryError
from src.utils.const import Constants
from .fmeta.model import FactoryMeta
from .errors import NewProjectError
from .fmeta.data import data
from utils.result import (
    Result,
    Err,
    Ok,
)


class NewProject(SafeClass):
    def __init__(self) -> None:
        super().__init__()

        ctt: Result = FileManager().read.as_list(
            name=Constants.START,
        )
        if ctt.is_err():
            self._use_error(ctt)
            return

        file_content: list[str] = ctt.value
        magic_word: str = file_content[0].strip()
        if not (magic_word in data):
            self._use_error(Err(error=FactoryError(
                message='Invalid fmt',
                call='NewProject()',
                source=__name__,
            )))
            return

        self._generators_metadata: list[FactoryMeta] = data[magic_word]
        self._content: list = file_content[1:]
        self._meta_content: dict = {}



    def build(self) -> Result[None, NewProjectError]:
        for line in self._content:
            action: Result = self._use_meta(line)
            if action.is_err():
                return action

        if not self._generators_metadata:
            return Ok()

        return Err(error=NewProjectError(
            message='Invalid document',
            call='NewProject.build',
            source=__name__,
        ))


    def _use_meta(self, content: str) -> Result[None, FactoryError | NewProjectError]:
        if not content:
            return Ok()

        for fact in self._generators_metadata:
            action: Result = fact.build(content=content)
            if action.is_ok():
                self._meta_content[fact._tag] = action.value

                if ',' in action.value:
                    new: list = self._meta_content[fact._tag].split(',')
                    self._meta_content[fact._tag] = new

                self._generators_metadata.remove(fact)
                return Ok()

        return Err(error=NewProjectError(
            message=f'Meta token not found, {content}',
            call='NewProject._use_meta',
            source=__name__,
        ))

