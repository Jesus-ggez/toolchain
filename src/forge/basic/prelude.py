#~>
from .errors import Error
from utils.result import (
    Result,
    Err,
    Ok,
)


class _:
    def _(self) -> Result[None, Exception]:
        ...
