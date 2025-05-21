#~>
from src.identity.dir_object import DirObject, DirVO
from src.core.safe_cls import SafeClass
from src.core.result import (
    Result,
    Err,
    Ok,
)


#.?
from .snippet_saver import SnippetSaver
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
            self.__use_data,
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
        if not isinstance(self._path, str) or self._path == '':
            return self.__create_error(msg='Invalid parameters')

        return Ok()


    def __create_data(self) -> Result[None, Exception]:
        data: DirObject = DirObject(dir_name=self._path)

        if ( err := data.check_error() ).is_err():
            return err

        self._data: DirVO = data.value

        return Ok()


    def __use_data(self) -> Result[None, ProjectError]:
        self._id_db: list[int] = []

        for item in self._data.content_vo:
            if ( err := item.check_error() ).is_err():
                print(err)
                continue

            snippet_data: SnippetSaver = SnippetSaver(data=item.value)
            if ( err := snippet_data.check_error() ).is_err():
                print(err)
                continue

            self._id_db.append(snippet_data.value)

        return Ok()


    def __create_struct_project(self) -> Result[None, ProjectError]:
        return self.__create_error('Not implemented')
        for item in self._data.dirs:
            ...


    def __(self) -> Result[None, ProjectError]:
        ...


