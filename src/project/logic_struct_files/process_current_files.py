#~>
from src.identity.file_object import FileObjectCreator
from src.core.safe_cls import SafeClass
from src.core.result import (
    Result,
    Err,
    Ok,
)


#.?
from .errs import ProjectError, TcErr


#<·


class ProcessCurrentFiles(SafeClass):
    def __init__(self, refr: list, items_to_process: list) -> None:
        super().__init__()

        self._data: list = []

        self._items_to_process: list = items_to_process

        self.__build()

        refr.extend(self._data)


    def __build(self) -> None:
        if ( err := self.__validate_parameters() ).is_err():
            return self._use_error(err)

        if ( err := self.__process_data() ).is_err():
            return self._use_error(err)


    def __validate_parameters(self) -> Result[None, ProjectError]:
        if not isinstance(self._items_to_process, list):
            return Err(error=ProjectError(
                message=f'Invalid type of items to process: {type(self._items_to_process)}',
                call='ProcessCurrentFiles()',
                source=__name__,
            ))

        return Ok()


    def __process_data(self) -> Result[None, ProjectError] | Result[None, TcErr]:
        items: list[str] = self._items_to_process

        for item in items:
            file_obj: FileObjectCreator = FileObjectCreator(file_name=item)

            if ( err := file_obj.check_error() ).is_err():
                return err

            self._data.append(file_obj.value)

        return Ok()


