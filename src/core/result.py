from typing import (
    NamedTuple,
    Generic,
    TypeVar,
    Any,
)


#~>


#<·
T = TypeVar('T', bound=Any)
E = TypeVar('E', bound=Exception)


class Result(NamedTuple, Generic[T, E]):
    ok: bool
    error: Any | E = None
    value: Any | T = None

    def is_ok(self) -> bool:
        return self.ok


    def is_err(self) -> bool:
        return not self.ok


    def __str__(self) -> str:
        return f'Ok(value={self.value})' if self.ok else f'Err(error={self.error})'


    def ensure_ok(self) -> None:
        if not self.ok:
            raise self.error

    def expect(self, message: str) -> None:
        print(f'Expect {message} -> ' + self.__str__())


def Ok(value: T = None) -> Result[T, E]:
    return Result(ok=True, value=value)


def Err(error: E) -> Result[T, E]:
    from nucleus.constants import TcConfig

    if TcConfig['details']:
        import traceback; traceback.print_exc()
    return Result(ok=False, error=error)
