#~>
from src.core.safe_cls import SafeClass
from utils.terminal import arguments
from src.core.result import Ok, Result


#<·
TcConfig: dict = {
    'not-null': False,
    'details': False,
    'errs': False,
}


class TcGlobalContext(SafeClass):
    def __init__(self) -> None:
        super().__init__()

        self._cases: list = []

        self.__build()


    def __build(self) -> None:
        if ( err := self.__filter_cases() ).is_err():
            return self._use_error(err)

        if ( err := self.__use_cases() ).is_err():
            return self._use_error(err)


    def __filter_cases(self) -> Result[None, Exception]:
        if not arguments: return Ok()

        for argument in arguments.copy():
            if not argument[0].isalnum():
                continue

            if not self.__exists_in_tcconfig(v=argument):
                continue

            self._cases.append(argument)
            arguments.remove(argument)

        return Ok()


    def __exists_in_tcconfig(self, v: str) -> bool:
        return v in TcConfig


    def __use_cases(self) -> Result[None, Exception]:
        for element in self._cases:
            TcConfig[element] = not TcConfig[element]

        return Ok()
