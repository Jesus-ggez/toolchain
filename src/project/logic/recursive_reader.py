from typing import Any
import os


#~>
from src.project.struct_repr.file_repr import CreatorFilesRepr
from src.project.struct_repr.dir_repr import CreatorDirsRepr
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

        self._current_context: Any = None

        self._path: str = path.strip()

        self.__build()


    def __build(self) -> None:
        for check in (
            self.__create_context,
            self.__create_recursion,
        ):
            if ( err := check() ).is_err():
                return self._use_error(err)


    def __create_context(self) -> Result[None, TcErr]:
        context: DirObject = DirObject(self._path)

        if ( err := context.check_error() ).is_err():
            return err

        self._current_context = context.value
        return Ok()


    def __create_recursion(self) -> Result[None, TcErr]:
        stack_pseudo_recursion: list[DirVO] = [self._current_context]
        register_of_repr: list[str] = []

        while True:
            # exit
            if not stack_pseudo_recursion:
                return Ok()

            # legibility
            dir_vo: DirVO = stack_pseudo_recursion[-1]

            # move to end node
            if dir_vo.dirs:
                self._path = dir_vo.dirs.pop()

                for check in (
                    self.___move_to,
                    self.__create_context,
                ):
                    if ( err := check() ).is_err():
                        return err

                stack_pseudo_recursion.append(self._current_context)
                continue

            # file representation
            ids: list = []
            for check in (
                self.___use_files,
                self.___create_ids,
            ):
                if ( err := check(ids) ).is_err():
                    return err

            # create final repr
            current_repr: str = dir_vo.name
            for check in (
                CreatorFilesRepr(items=ids),
                CreatorDirsRepr(items=register_of_repr),
            ):
                if ( err := check.check_error() ).is_err():
                    return err

                current_repr += check.value

            ...


    def ___use_files(self, ids_refr: list) -> Result[None, TcErr]:
        for file_name in self._current_context.files:
            vo_value: FileObject = FileObject(file_name=file_name)

            if ( err := vo_value.check_error() ).is_err():
                return err

            ids_refr.append(vo_value.value)

        return Ok()


    def ___create_ids(self, ids_refr: list) -> Result[None, TcErr]:
        new_data: list = []

        for numeric_id in ids_refr:
            new_id: SnippetSaver = SnippetSaver(numeric_id)

            if ( err := new_id.check_error() ).is_err():
                return err

            new_data.append(new_id.value)

        ids_refr = new_data
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

