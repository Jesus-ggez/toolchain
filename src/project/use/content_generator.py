#~>
from src.core.safe_cls import SafeClass
from src.core.result import (
    Result,
    Err,
    Ok,
)


#.?
from .factories.get_factory import SKWFactory
from .tokenizer import tokenize
from .errs import UseError
from .tc_ast import TcAST


#<·
class ContentGenerator(SafeClass):
    def __init__(self, struct: str) -> None:
        super().__init__()

        self._tokens: list[str] = []
        self._struct: str = struct
        print(self._struct)

        self.__build()


    def __build(self) -> None:
        if ( err := self.__validate_parameters() ).is_err():
            return self._use_error(err)

        if ( err := self.__main_loop() ).is_err():
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


    def __main_loop(self) -> Result[None, UseError]:
        local_ast: type[TcAST] = TcAST

        print(self._tokens)
        for token in self._tokens:
            if '_' in token:
                local_ast.last_token = token
                continue

            if token.isalnum():
                local_ast.last_token = token
                continue

            actor: Result = SKWFactory.get_factory(key=token)

            if actor.is_err():
                return actor

            actor.value(
                context=local_ast,
            )
        return Ok()
