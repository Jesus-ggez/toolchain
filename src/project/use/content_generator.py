#~>
from src.core.safe_cls import SafeClass
from utils.tokens import tokenize
from src.core.result import (
    Result,
    Err,
    Ok,
)


#.?
from .errs import UseError


#<·
class ContentGenerator(SafeClass):
    def __init__(self, struct: str) -> None:
        super().__init__()

        self._tokens: list[str] = []
        self._struct: str = struct

        self.__build()


    def __build(self) -> None:
        if ( err := self.__validate_parameters() ).is_err():
            return self._use_error(err)


    def __create_error(self, msg: str) -> Result[None, UseError]:
        return Err(error=UseError(
            call='ProjectUseWorkspace()',
            source=__name__,
            message=msg,
        ))


    def __validate_parameters(self) -> Result[None, UseError]:
        if not isinstance(self._struct, str) or not self._struct:
            return self.__create_error('Invalid project struct')

        self._tokens.extend(tokenize(self._struct))

        return Ok()

