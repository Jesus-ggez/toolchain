from typing import (
    NamedTuple,
    Optional,
    Generic,
    TypeVar,
)


T = TypeVar('T')
E = TypeVar('E', bound=Exception)


class Result(NamedTuple, Generic[T, E]):
    ok: bool
    error: Optional[E] = None
    data: Optional[T] = None

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

