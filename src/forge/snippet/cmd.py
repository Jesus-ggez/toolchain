#~>
from utils.terminal import get_copy_next_arg, get_next_arg
from .errors import TerminalError
from utils.result import (
    Result,
    Err,
    Ok,
)


class Terminal:
    @staticmethod
    def get_tempname() -> Result[str, TerminalError]:
        _value: Result = get_copy_next_arg()
        if _value.is_err():
            return Err(error=TerminalError(
                message='Invalid Argument',
            ))

        value: Result = get_next_arg()
        if value.is_err():
            return Err(error=TerminalError(
                message='Unknown Error, copy != original',
            ))

        if value.data != _value.data:
            return Err(error=TerminalError(
                message='Unknown Error, copy != original',
            ))

        if not value.data.startswith('--'):
            return Err(error=TerminalError(
                message='Invalid Flag'
            ))

        flag: str = value.data.removeprefix('--')
        if not flag.startswith('tempname'):
            return Err(error=TerminalError(
                message='Invalid flag name'
            ))

        kv: list = flag.split('[')
        if len(kv) != 2:
            return Err(error=TerminalError(
                message='Invalid syntax',
            ))

        tempname: str = kv[1]
        if not tempname.endswith(']'):
            return Err(error=TerminalError(
                message='Invalid syntax',
            ))

        return Ok(tempname.removesuffix(']'))
