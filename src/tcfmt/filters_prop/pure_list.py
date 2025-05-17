#~>
from src.core.result import (
    Result,
    Err,
    Ok,
)


#.?
from .errs import FilterPropertyError
from .pure_str import filt_str


#<·
def filt_list(v: str) -> Result[list, FilterPropertyError]:
    # " [  ]" -> '' | '' == False -> Err
    pure_values: str = v.strip('[]').strip()

    if not pure_values:
        return Err(error=FilterPropertyError(
            message=f'Invalid content: {v.strip('"')}',
            call='fn::filt_list',
            source=__name__,
        ))

    end_values: list[str] = []

    for value in pure_values.split(','):
        if ( val := filt_str(v=value) ).is_ok():
            end_values.append(val.value)
            continue

    return Ok(end_values)
