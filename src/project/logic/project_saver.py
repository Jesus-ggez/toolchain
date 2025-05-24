#~>
from src.core.safe_cls import SafeClass
from src.core.result import (
    Result,
    Err,
    Ok,
)


#.?
from .errs import ProjectError


#<·
class ProjectSaver(SafeClass):
    def __init__(self, path: str) -> None:
        super().__init__()

        self._path: str = path.strip()
        self._project_dirs: list = []
        self._context: dict = {}

        self.__build()


    def __build(self) -> None:
        for check in (
            self.__validate_parameters,
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



















