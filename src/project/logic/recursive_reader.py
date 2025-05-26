from typing import Any
import os


#~>
from src.project.struct_repr.file_repr import CreatorFilesRepr
from src.project.struct_repr.dir_repr import CreatorDirsRepr
from src.identity.dir_object import DirObject, DirVO
from src.identity.file_object import FileObject
from src.core.errors import TcErr, safe_exec
from src.core.safe_cls import SafeClass
from nucleus.prelude import TcLog
from src.core.result import (
    Result,
    Ok,
)


#.?
from .discard_ignored_values import discard_values
from .snippet_saver import SnippetSaver


#<·
class RecursiveReader(SafeClass):
    def __init__(self, path: str, ignore: list) -> None:
        super().__init__()

        self._ignore: list[str] = ignore
        self._path: str = path.strip()

        self._mut_curr_dir_space: Any = None

        self.__build()


    def __build(self) -> None:
        if ( err := self.__create_directory(self._path) ).is_err():
            return self._use_error(err)

        if ( err := self.__create_recursion() ).is_err():
            return self._use_error(err)


    def __create_directory(self, path: str) -> Result[None, TcErr]:
        dir_space: DirObject = DirObject(dir_name=path)

        if ( err := dir_space.check_error() ).is_err():
            return err

        discard_values(item_refr=dir_space.value, ignored=self._ignore)

        self._mut_curr_dir_space = dir_space.value
        return Ok()


    def __create_recursion(self) -> Result[None, TcErr]:
        stack: list[tuple] = [
            ( self._mut_curr_dir_space, [] )
        ]

        while True:
            if not stack:
                break

            item_stack: tuple[DirVO, list] = stack[-1]

            if item_stack[0].dirs:
                if ( err := self.__create_directory(path=item_stack[0].dirs.pop()) ).is_err():
                    return err

                new_stack_item: tuple = (self._mut_curr_dir_space, [])
                stack.append(new_stack_item)

                continue

            raw_file_repr: list = []
            if ( err := self.___use_files_from_curr_dir_space(refr=raw_file_repr) ).is_err():
                return err

            if ( err := self.___process_current_files(refr=raw_file_repr) ).is_err():
                return err

            node_repr: str = item_stack[0].name

            node_repr_content: Result = self.___create_node_repr(
                dirs_data=item_stack[1],
                file_data=raw_file_repr,
            )

            if node_repr_content.is_err():
                return node_repr_content

            node_repr += node_repr_content.value

            TcLog(stack)
            TcLog(node_repr)

            stack.pop()
            if not stack:
                self._value = node_repr
                break

            self._mut_curr_dir_space, storage = stack[-1]
            storage.append(node_repr)

            if ( err := self.___move_out() ).is_err():
                return err

        return Ok()


    def ___use_files_from_curr_dir_space(self, refr: list) -> Result[None, TcErr]:
        data: list[str] = self._mut_curr_dir_space.files

        for item in data:
            file_obj: FileObject = FileObject(file_name=item)

            if ( err := file_obj.check_error() ).is_err():
                return err

            refr.append(file_obj.value)


        return Ok()


    def ___process_current_files(self, refr: list) -> Result[None, TcErr]:
        ids: list[str] = []

        for item in refr:
            id_snippet: SnippetSaver = SnippetSaver(data=item)

            if ( err := id_snippet.check_error() ).is_err():
                return err

            ids.append(id_snippet.value)

        refr.clear()
        refr.extend(ids)

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
