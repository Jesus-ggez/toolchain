#~>
from src.core.safe_cls import SafeClass
from src.core.result import (
    Result,
    Ok,
)


#.?
from .errs import RepresentationError


#<·
class NodeReprCreator(SafeClass):
    def __init__(self, nodes: list[str], files: list[str], name: str) -> None:
        super().__init__()

        self._file_repr: str = ''
        self._dir_repr: str = ''
        self._value: str = name.strip()

        self._nodes: list[str] = nodes
        self._files: list[str] = files

        self.__build()


    def __build(self) -> None:
        if ( err := self.__use_files() ).is_err():
            return self._use_error(err)

        if ( err := self.__use_dir_nodes() ).is_err():
            return self._use_error(err)

        if ( err := self.__create_node_repr() ).is_err():
            return self._use_error(err)



    def __use_files(self) -> Result[None, RepresentationError]:
        if not self._files:
            return Ok()

        comma: str = ','
        items: str = comma.join(self._files).strip()
        value: str = items.removeprefix(comma).removesuffix(comma)

        self._file_repr += value

        return Ok()


    def __use_dir_nodes(self) -> Result[None, RepresentationError]:
        if not self._nodes:
            return Ok()

        self._dir_repr += ''.join(self._nodes)
        return Ok()


    def __create_node_repr(self) -> Result[None, RepresentationError]:
        if not self._file_repr and not self._dir_repr:
            self._value += '.'
            return Ok()

        self._value += '{'

        if not self._file_repr:
            self._value += self._dir_repr + '}'
            return Ok()

        if not self._dir_repr:
            self._value += self._file_repr + '}'
            return Ok()

        self._value += self._file_repr + ';'
        self._value += self._dir_repr + '}'

        return Ok()

    @property
    def value(self) -> str:
        return self._value
