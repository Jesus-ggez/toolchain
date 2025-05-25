from typing import Any
import os


#~>
from src.project.struct_repr.file_repr import CreatorFilesRepr
from src.project.struct_repr.dir_repr import CreatorDirsRepr
from src.identity.dir_object import DirObject, DirVO
from src.identity.file_object import FileObject
from src.core.errors import TcErr, safe_exec
from src.core.safe_cls import SafeClass
from src.core.result import (
    Result,
    Ok,
)


#.?
from .snippet_saver import SnippetSaver


#<·
class RecursiveReader(SafeClass):
    def __init__(self, path: str, ignore: list) -> None:
        super().__init__()

        self._temporal_file_repr: list = []
        self._current_context: Any = None

        self._path: str = path.strip()
        self._ignore: list[str] = ignore

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

        if ( err := self.__ignore_items() ).is_err():
            return err

        print(self._current_context)
        return Ok()


    def __create_recursion(self) -> Result[None, TcErr]:
        stack_pseudo_recursion: list[tuple[DirVO, list]] = [
            (self._current_context, []),
        ]

        while True:
            print(len(stack_pseudo_recursion))
            if not stack_pseudo_recursion:
                break

            dir_obj, dirs_stack = stack_pseudo_recursion[-1]

            # create moviment to end node
            if dir_obj.dirs:
                self._path = dir_obj.dirs.pop()

                if ( err := self.__create_context() ).is_err():
                    return err

                stack_pseudo_recursion.append(
                    (self._current_context, []),
                )
                continue

            # process file content
            if ( err := self.___create_file_repr_content() ).is_err():
                return err

            if ( err := self.___create_file_repr_ids() ).is_err():
                return err

            # create repr
            node_repr: str = dir_obj.name
            for check in (
                CreatorFilesRepr(items=self._temporal_file_repr),
                CreatorDirsRepr(items=dirs_stack),
            ):
                if ( err := check.check_error() ).is_err():
                    return err

                node_repr += check.value

            # final repr
            stack_pseudo_recursion.pop()
            if not stack_pseudo_recursion:
                print(node_repr)
                break

            self._current_context, storage = stack_pseudo_recursion[-1]

            storage.append(node_repr)

            if ( err := self.__move_out() ).is_err():
                return err

        return Ok()



    def ___create_file_repr_content(self) -> Result[None, TcErr]:
        data: list = self._current_context.files

        self._temporal_file_repr.clear()

        for item in data:
            obj: FileObject = FileObject(item)
            if ( err := obj.check_error() ).is_err():
                return err

            self._temporal_file_repr.append(obj.value)

        return Ok()


    def ___create_file_repr_ids(self) -> Result[None, TcErr]:
        ids: list[str] = []

        for item in self._temporal_file_repr:
            data: SnippetSaver =  SnippetSaver(item)

            if ( err := data.check_error() ).is_err():
                return err

            ids.append(data.value)

        self._temporal_file_repr.clear()
        self._temporal_file_repr.extend(ids)

        return Ok()


    def __ignore_items(self) -> Result[None, TcErr]:
        for item in self._ignore:

            if item.endswith('*'):
                begin: str = item.removesuffix('*')

                for item in self._current_context.dirs:
                    if item.startswith(begin):
                        self._current_context.dirs.remove(item)

                continue

            if item in self._current_context.dirs:
                self._current_context.dirs.remove(item)


        return Ok()


    @safe_exec
    def __move_out(self) -> Any:
        return os.chdir('..')
