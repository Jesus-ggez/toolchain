from typing import Any
import os


#~>
from src.identity.dir_object import DirObjectCreator, DirVO
from src.core.errors import TcErr, safe_exec
from src.core.safe_cls import SafeClass
from nucleus.prelude import TcLog
from src.core.result import (
    Result,
    Ok,
)


#.?
from .struct_repr.file_repr import CreatorFilesRepr
from .struct_repr.dir_repr import CreatorDirsRepr
from .discard_values import discard_values
from .process_files import ProcessFiles


#<·
class RecursiveReader(SafeClass):
    def __init__(self, path: str, ignore: list) -> None:
        super().__init__()

        self._ignore: list[str] = ignore
        self._path: str = path.strip()

        self._current_tree: DirVO | Any = Any

        self.__build()


    def __build(self) -> None:
        if ( err := self.__create_directory(self._path) ).is_err():
            return self._use_error(err)

        if ( err := self.__create_recursion() ).is_err():
            return self._use_error(err)


    def __create_directory(self, path: str) -> Result[None, TcErr]:
        dir_space: DirObjectCreator = DirObjectCreator(dir_name=path)

        if ( err := dir_space.check_error() ).is_err():
            return err

        discard_values(item_refr=dir_space.value, ignored=self._ignore)

        self._current_tree = dir_space.value
        return Ok()


    def __create_recursion(self) -> Result[None, TcErr]:
        stack: list[tuple] = [
            ( self._current_tree, [] )
        ]

        while True:
            if not stack:
                break

            item_stack: tuple = stack[-1]

            tree: DirVO = item_stack[0]

            if tree.dirs:
                if ( err := self.__create_directory(path=tree.dirs.pop()) ).is_err():
                    return err

                stack.append( ( self._current_tree, [] ) )
                continue

            procesed_files: ProcessFiles = ProcessFiles(
                files=tree.files,
            )

            if ( err := procesed_files.check_error() ).is_err():
                return err

            node_repr_content: Result = self.___create_node_repr(
                file_data=procesed_files.value,
                dirs_data=item_stack[1],
            )

            if node_repr_content.is_err():
                return node_repr_content

            node_repr: str = tree.name + node_repr_content.value

            TcLog((stack, node_repr))

            stack.pop()
            if not stack:
                self._value = node_repr
                break

            self._current_tree, storage = stack[-1]
            storage.append(node_repr)

            if ( err := self.___move_out() ).is_err():
                return err

        return Ok()


    def ___create_node_repr(self, file_data: list, dirs_data: list) -> Result[str, TcErr]:
        files_repr: CreatorFilesRepr = CreatorFilesRepr(items=file_data)
        dirs_repr: CreatorDirsRepr = CreatorDirsRepr(items=dirs_data)

        if ( err := files_repr.check_error() ).is_err():
            return err

        if ( err := dirs_repr.check_error() ).is_err():
            return err

        return Ok(files_repr.value + dirs_repr.value)


    @safe_exec
    def ___move_out(self) -> Any:
        return os.chdir('..')


    @property
    def value(self) -> str:
        return self._value

