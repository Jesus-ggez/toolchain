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
    if not v.strip('"'):
        return Err(error=FilterPropertyError(
            message=f'Invalid content: {v.strip('"')}',
            call='fn::filt_str',
            source=__name__,
        ))

    print(v, 'ok')
    return Ok(v.strip('"').strip())
