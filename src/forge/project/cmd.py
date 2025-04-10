#~>
from utils.terminal import get_copy_next_arg, get_next_arg
from .errors import TerminalError
from utils.result import (
    Result,
    Err,
    Ok,
)


class Terminal:
    PREFIX_NAME: str = '--tempname'
    PREFIX_ALIAS: str = '--alias'
    DEFAULT_NAME: str = '_'
    DIVIDER: str = '-'


    @staticmethod
    def get_name() -> Result[str, TerminalError]:
        _content: Result = get_copy_next_arg()
        if _content.is_err():
            return Ok(Terminal.DEFAULT_NAME)

        get_next_arg()
        content: str = _content.value
        if not content.startswith(Terminal.PREFIX_NAME):
            return Err(error=TerminalError(
                call='Terminal.get_name',
                message='Invalid flag',
                source=__name__,
            ))

        raw_content: str = content.removeprefix(Terminal.PREFIX_NAME)
        pre_final: list[str] = raw_content.split(Terminal.DIVIDER)

        if len(pre_final) != 2:
            return Err(error=TerminalError(
                message='Invalid format of flag',
                call='Terminal.get_name',
                source=__name__,
            ))

        final: str = pre_final[1]
        return Ok(final)


    @staticmethod
    def get_alias() -> str:
        if get_copy_next_arg().is_err():
            return Terminal.DEFAULT_NAME

        content: str = get_next_arg().value

        if not content.startswith(Terminal.PREFIX_ALIAS):
            return Terminal.DEFAULT_NAME

        raw_content: str = content.removeprefix(Terminal.PREFIX_ALIAS)
        pre_final: list[str] = raw_content.split(Terminal.DIVIDER)

        if len(pre_final) != 2:
            return Terminal.DEFAULT_NAME

        final: str = pre_final[1]
        return final
