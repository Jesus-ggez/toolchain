#~>
from src.tcfiles.data import data_templates
from src.core.errs import FileWriterError
from src.core.safe_cls import SafeClass
from src.core.file_utils import Writer
from src.core.result import (
    Result,
    Err,
    Ok,
)


#.?
from .errs import TcTcfmtCreatorError
from .constants import TcConfig


#<·
class TcFileCreator(SafeClass):
    def __init__(self, root: str, tempname: str) -> None:
        super().__init__()

        self._tempname: str = tempname
        self._root: str = root

        self.__build()


    def __build(self) -> None:
        for check in (
            self.__validate_parameters,
            self.__validate_node,
        ):
            if ( err := check() ).is_err():
                return self._use_error(err)

        self._data_templates: dict = data_templates[self._root]

        for check in (
            self.__validate_template_exists,
            self.__use_template,
        ):
            if ( err := check() ).is_err():
                return self._use_error(err)


    def __create_error(self, msg: str) -> Result[None, TcTcfmtCreatorError]:
        return Err(error=TcTcfmtCreatorError(
            call='TcFileCreator()',
            source=__name__,
            message=msg,
        ))


    def __validate_parameters(self) -> Result[None, TcTcfmtCreatorError]:
        if not self._root or not self._tempname:
            return self.__create_error(msg='Invalid parameters')
        return Ok()


    def __validate_node(self) -> Result[None, TcTcfmtCreatorError]:
        if not self._root in data_templates:
            return self.__create_error(msg='Invalid node name for tempname tree use')

        return Ok()


    def __validate_template_exists(self) -> Result[None, TcTcfmtCreatorError]:
        if not self._tempname in self._data_templates:
            return self.__create_error(msg='Invalid template name')

        return Ok()


    def __use_template(self) -> Result[None, FileWriterError]:
        if ( err := Writer.from_str(
            content=self._data_templates[self._tempname],
            name=TcConfig.FILE_NAME,
        ) ).is_err():
            return err

        return Ok()
