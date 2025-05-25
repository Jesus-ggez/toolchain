#~>
from src.core.safe_cls import SafeClass
from src.core.result import (
    Result,
    Err,
    Ok,
)


#.?
from .recursive_reader import RecursiveReader
from .errs import ProjectError


#<·
class ProjectSaver(SafeClass):
    def __init__(self, metadata: dict) -> None:
        super().__init__()

        self._ignore: list = metadata.get('ignore', [])

        self._path: str = metadata.get('target', '')
        self._project_dirs: list = []
        self._context: dict = {}

        self.__build()


    def __build(self) -> None:
        for check in (
            self.__validate_parameters,
            self.__create_reader,
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


    def __create_reader(self) -> Result[None, ProjectError]:
        if ( err := RecursiveReader(path=self._path, ignore=self._ignore).check_error() ).is_err():
            return err

        return Ok()














