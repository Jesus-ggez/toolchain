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
    DEFAULT_NAME: str = '_'
    PREFIX: str = '--name'
    DIVIDER: str = '-'


    @staticmethod
    def get_name() -> Result[str, TerminalError]:
        _name: Result = get_copy_next_arg()
        if _name.is_err():
            return Ok('blank')

        get_next_arg()
        name: str = _name.value
        if name == '--help':
            print_help()
            return Ok(Terminal.DEFAULT_NAME)

        if not name.startswith(Terminal.PREFIX):
            return Err(error=TerminalError(
                'Expected "--name-value", got something else',
            ))

        cmd: str = name.removeprefix(Terminal.PREFIX)
        content: list[str] = cmd.split(Terminal.DIVIDER)

        if len(content) != 2:
            return Err(error=TerminalError(
                'Invalid syntax in "{name}"',
            ))

        return Ok(content[1])

