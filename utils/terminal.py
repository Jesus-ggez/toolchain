from sys import argv as arguments

#~>
from utils.result import (
    Result,
    Err,
    Ok,
)


def is_empty_cmd() -> bool:
    return not arguments


def get_next_arg() -> Result[str, Exception]:
    if is_empty_cmd():
        return Err(error=ValueError(
            'Not found arguments'
        ))

    return Ok(data=arguments.pop(0))


def get_copy_next_arg() -> Result[str, Exception]:
    if is_empty_cmd():
        return Err(error=ValueError(
            'Not found next argument to copy'
        ))

    return Ok(data=arguments[0])
