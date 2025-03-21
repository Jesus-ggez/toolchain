#~>
from .result import Result, Err, Ok
from .errors import (
    safe_exec
)


class _:
    def _(self) -> Result[None, Exception]:
        ...
