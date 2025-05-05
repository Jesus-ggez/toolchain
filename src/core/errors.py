# import traceback

#~>
from .result import (
    Result,
    Err,
    Ok,
    T,
)


#<·
class TcErr(Exception):
    def __init__(self, source: str, call: str, message: str) -> None:
        msg: str = f'{source} | {call} | {message}'
        super().__init__(msg)

class BaseError(TcErr): ...


def safe_exec(func):
    def wrapper(*args, **kwargs) -> Result[T, Exception]:
        try:
            result = func(*args, **kwargs)
            return Ok(result)

        except Exception as e:
            #traceback.print_exc()
            return Err(e)
    return wrapper

