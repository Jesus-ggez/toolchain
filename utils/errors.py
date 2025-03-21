from .result import (
    Result,
    Err,
    Ok,
    T,
)


def safe_exec(func):
    def wrapper(*args, **kwargs) -> Result[T, Exception]:
        try:
            result = func(*args, **kwargs)
            return Ok(result)

        except Exception as e:
            return Err(e)

    return wrapper
