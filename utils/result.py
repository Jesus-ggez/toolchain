from typing import (
    NamedTuple,
    Generic,
    TypeVar,
    Any,
)


T = TypeVar('T', bound=Any)
E = TypeVar('E', bound=Exception)


class Result(NamedTuple, Generic[T, E]):
    ok: bool
    error: Any | E = None
    data: Any | T = None

    def is_ok(self) -> bool:
        return self.ok


    def is_err(self) -> bool:
        return not self.ok


    def __str__(self) -> str:
        if self.ok:
            return f'Ok(data={self.data})'
        return f'Err(error={self.error})'


def Ok(data: T = None) -> Result[T, E]:
    return Result(ok=True, data=data)


def Err(error: E) -> Result[T, E]:
    return Result(ok=False, error=error)

