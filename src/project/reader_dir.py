import os


#~>
from src.identity.file_object import FileObject, FileVO
from src.identity.dir_object import DirObject, DirVO
from src.core.safe_cls import SafeClass
from src.core.errors import TcErr
from src.core.result import (
    Result,
    Err,
    Ok,
)


#.?
from .snippet_saver import SnippetSaver


#<·
class RecursiveReader(SafeClass):
    def __init__(self, path: str) -> None:
        super().__init__()

        self._context_vo: list[FileVO] = []

        self._context: DirVO | None = None
        self._repr_struct: list[str] = []
        self._path: str = path.strip()
        self._dirs_stack_: list = []

        self.__build()


    def __build(self) -> None:
        for check in (
            # create_initial_context
            self.__create_context,

            self.__create_recursion,
        ):
            if ( err := check() ).is_err():
                return self._use_error(err)


    def __create_context(self) -> Result[None, TcErr]:
        current_context: DirObject = DirObject(self._path)

        if ( err := current_context.check_error() ).is_err():
            return err

        self._context: DirVO = current_context.value
        self._dirs_stack_.append(self._context)

        return Ok()


    def __create_recursion(self) -> Result[None, TcErr]:
        while True:
            if not self._dirs_stack_:
                break

            if self._context.dirs:
                if ( err := self.___pre_contextual() ).is_err():
                    return err

                continue

            if self._context.files:
                if ( err := self.___create_file_value_objects() ).is_err():
                    return err

            if ( err := self.___create_repr() ).is_err():
                return err

            self._context = self._dirs_stack_.pop()

        return Ok()


    def ___pre_contextual(self) -> Result[None, TcErr]:
        self._path = self._context.dirs.pop(0)

        for check in (
            self.___move_to,
            self.__create_context,
        ):
            if ( err := check() ).is_err():
                return err

        return Ok()


    def ___create_file_value_objects(self) -> Result[None, TcErr]:
        self._context_vo: list = []
        for item in self._context.files:
            vo: FileObject = FileObject(file_name=item)

            if ( err := vo.check_error() ).is_err():
                return err

            self._context_vo.append(vo.value)

        return Ok()


    def ___move_to(self) -> Result[None, TcErr]:
        try:
            os.chdir(self._path)
            return Ok()

        except Exception as e:
            os.chdir('..')
            return Err(error=TcErr(
                call='RecursiveReader()',
                source=__name__,
                message=str(e),
            ))


    def ___create_repr(self) -> Result[None, TcErr]:
        base: str = self._context.name
        ids: list[str] = []

        if not self._context_vo:
            self._repr_struct.append(base + ',')
            return Ok()

        for item in self._context_vo:
            record_id: SnippetSaver = SnippetSaver(data=item)

            if ( err := record_id.check_error() ).is_err():
                return err

            ids.append(record_id.value)

        base += '[' + ','.join(ids) + ']'

        self._repr_struct.append(base.replace('[,', '[').replace(',]', ']') )

        return Ok()
