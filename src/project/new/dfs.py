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
from .struct_repr.node_repr_creator import NodeReprCreator
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

            # vars
            tree: DirVO = stack[-1][0]

            if tree.dirs:
                if ( err := self.__create_directory(path=tree.dirs.pop()) ).is_err():
                    return err

                stack.append( ( self._current_tree, [] ) )
                continue

            # filespace
            local_node_storage: list[str] = stack[-1][1]

            files_processed: ProcessFiles = ProcessFiles(
                files=tree.files,
            )
            if ( err := files_processed.check_error() ).is_err():
                return err

            # general nodespace
            action_node_repr: NodeReprCreator = NodeReprCreator(
                files=files_processed.value,
                nodes=local_node_storage,
                name=tree.name,
            )
            if ( err := action_node_repr.check_error() ).is_err():
                return err

            node_repr: str = action_node_repr.value

            # logs
            TcLog(node_repr)

            # end actions in this node
            stack.pop()

            if not stack:
                self._value: str = node_repr
                break

            local_node_storage: list[str] = stack[-1][1]
            local_node_storage.append(node_repr)

            if ( err := self.___move_out() ).is_err():
                return err

        return Ok()


    @safe_exec
    def ___move_out(self) -> Any:
        return os.chdir('..')


    @property
    def value(self) -> str:
        return self._value

