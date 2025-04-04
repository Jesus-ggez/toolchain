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
    @staticmethod
    def get_name() -> Result[str, TerminalError]:
        _name: Result = get_copy_next_arg()
        if _name.is_err():
            return Ok('blank')

        get_next_arg()
        name: str = _name.value
        if name == '--help':
            print_help()
            return Ok('_')

        divider: str = '-'
        prx: str = '--name'
        if not name.startswith(prx):
            return Err(error=TerminalError(
                'Invalid argument',
            ))

        cmd: str = name.removeprefix(prx)
        content: list[str] = cmd.split(divider)

        if len(content) != 2:
            return Err(error=TerminalError(
                'Invalid syntax',
            ))

        final: str = content[1]

        return Ok(final)

