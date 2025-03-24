from utils.result import Result, Err


def use_alias() -> Result[None, Exception]:
    return Err(error=NotImplementedError(
        'impl in the future'
    ))
