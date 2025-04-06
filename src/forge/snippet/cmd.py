#~>
from utils.terminal import get_copy_next_arg, get_next_arg
from .start.utils import print_help
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
        _name: Result = get_copy_next_arg()
        if _name.is_err():
            return Ok('blank')

        name: str = _name.value
        if name == '--help':
            print_help()
            return Ok(Terminal.DEFAULT_NAME)

        get_next_arg()

        if not name.startswith(Terminal.PREFIX_NAME):
            return Err(error=TerminalError(
                message=f'Expected "{Terminal.PREFIX_NAME}-value", got something else',
                call='Terminal.get_name',
                source=__name__,
            ))

        cmd: str = name.removeprefix(Terminal.PREFIX_NAME)
        content: list[str] = cmd.split(Terminal.DIVIDER)

        if len(content) != 2:
            return Err(error=TerminalError(
                message=f'Invalid syntax in {name}',
                call='Terminal.get_name',
                source=__name__,
            ))

        final: str = content[1]

        return Ok(final)


    @staticmethod
    def get_alias() -> str:
        copy: Result = get_copy_next_arg()
        if copy.is_err():
            return ''

        get_next_arg()
        value: str = copy.value
        if not value.startswith(Terminal.PREFIX_ALIAS):
            return ''

        content: list = value.removeprefix(Terminal.PREFIX_ALIAS).split(Terminal.DIVIDER)
        if len(content) != 2:
            return ''

        final: str = content[1]

        return final
