#~>
from src.core.result import (
    Result,
    Err,
    Ok,
)


#.?
from .errs import FilterPropertyError


#<·
def filt_str(v: str) -> Result[str, FilterPropertyError]:
    val: str = v.strip('"').strip()

    if not val:
        return Err(error=FilterPropertyError(
            message=f'Invalid content: {v.strip('"')}',
            call='fn::filt_str',
            source=__name__,
        ))

    return Ok(val)
