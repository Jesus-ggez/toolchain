#~>
from utils.terminal import get_copy_next_arg, get_next_arg
from .errors import TerminalError
from utils.result import (
    Result,
    Err,
    Ok,
)


class Terminal:
    def get_manager(self) -> Result[str, TerminalError]:
        _arg: Result = get_copy_next_arg()
        if _arg.is_err():
            return Err(error=TerminalError(
                message='Not arguments',
            ))

        if not _arg.data.startswith('--'):
            return Err(error=TerminalError(
                message='Invalid flag',
            ))

        flag: str = _arg.data.removeprefix('--')
        get_next_arg()

        return Ok(data=flag)
