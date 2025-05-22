#~>
from src.identity.dir_object import DirObject #, DirVO
from src.core.safe_cls import SafeClass
from src.core.errors import TcErr
from src.core.result import (
    Result,
    Err,
    Ok,
)


#.?
#from .snippet_saver import SnippetSaver
from .errs import ProjectError


#<·
class ProjectSaver(SafeClass):
    def __init__(self, path: str) -> None:
        super().__init__()

        self._path: str = path.strip()

        self.__build()


    def __build(self) -> None:
        for check in (
            self.__validate_parameters,
            self.__create_data,
        ):
            if ( err := check() ).is_err():
                return self._use_error(err)


    def __create_error(self, msg: str) -> Result[None, ProjectError]:
        return Err(error=ProjectError(
            call='ProjectSaver()',
            source=__name__,
            message=msg
        ))


    def __validate_parameters(self) -> Result[None, ProjectError]:
        if not isinstance(self._path, str) or not self._path:
            return self.__create_error(msg='Invalid parameters')

        return Ok()


    def __create_data(self) -> Result[None, TcErr]:
        data: DirObject = DirObject(self._path)

        if ( err := data.check_error() ).is_err():
            return err

        return Ok()
