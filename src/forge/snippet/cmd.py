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

        name: str = _name.value
        if name == '--help':
            print_help()
            return Ok('_')

        if name != get_next_arg().value:
            return Err(error=TerminalError(
                'Unknown Error, get_next_arg != get_copy_next_arg',
            ))
        if not name.startswith('--'):
            return Err(error=TerminalError(
                'Invalid argument',
            ))

        cmd: str = name.removeprefix('--')
        content: list[str] = cmd.split(sep='[')

        if len(content) != 2 or not content[1].endswith(']'):
            return Err(error=TerminalError(
                'Invalid syntax',
            ))

        final: str = content[1].removesuffix(']')

        return Ok(final)
