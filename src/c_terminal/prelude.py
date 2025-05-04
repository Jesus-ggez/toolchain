#~>
from utils.terminal import get_copy_next_arg, get_next_arg
from src.core.safe_cls import SafeClass
from src.core.result import (
    Result,
    Err,
    Ok,
)

#.?
from .errs import TerminalError

#<·
class Terminal(SafeClass):
    def __init__(self, field: str) -> None:
        super().__init__()

        if not field:
            self._use_error(Err(error=TerminalError(
                message='Unknown field name',
                call='Terminal()',
                source=__name__,
            )))

        self._divider: str = '-'
        self._field: str = field


    def get_field(self) -> Result[str, TerminalError]:
        arg: Result = get_copy_next_arg()
        if arg.is_err():
            return Ok('_')

        get_next_arg()
        raw_value: str = arg.value

        if not raw_value.startswith(self._field):
            return Err(error=TerminalError(
                message='Invalid fmt to flag',
                call='Terminal.get_field',
                source=__name__,
            ))

        parts: list[str] = raw_value.removeprefix(
            self._field,
        ).split(sep=self._divider)

        if len(parts) != 2:
            return Err(error=TerminalError(
                message='Invalid terminal value',
                call='Terminal.get_field',
                source=__name__,
            ))

        if not parts[1]:
            return Err(error=TerminalError(
                message=f'Invalid value for {self._field}',
                call='Terminal.get_field',
                source=__name__,
            ))

        final: str = parts[1]
        return Ok(final)
