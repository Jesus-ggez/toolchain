#~>
from utils.terminal import get_copy_next_arg, get_next_arg
from .errors import TerminalError
from utils.result import (
    Result,
    Err,
    Ok,
)


class Terminal:
    PREFIX_NAME: str = '--name'
    DEFAULT_NAME: str = '_'
    DIVIDER: str = '-'


    @staticmethod
    def get_name() -> Result[str, TerminalError]:
        copy: Result = get_copy_next_arg()
        if copy.is_err():
            return Ok(Terminal.DEFAULT_NAME)

        get_next_arg()
        value: str = copy.value

        if not value.startswith(Terminal.PREFIX_NAME):
            return Err(error=TerminalError(
                call='Terminal.get_name',
                message='Invalid flag',
                source=__name__,
            ))

        data: list = value.removeprefix(Terminal.PREFIX_NAME).split(Terminal.DIVIDER)
        if len(data) != 2:
            return Err(error=TerminalError(
                message='Invalid arguments',
                call='Terminal.get_name',
                source=__name__,
            ))

        final: str = data[1]

        return Ok(final)
