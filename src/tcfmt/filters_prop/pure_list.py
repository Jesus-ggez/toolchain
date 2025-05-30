#~>
from src.core.result import (
    Result,
    Ok,
)


#.?
from .errs import FilterPropertyError
from .pure_str import filt_str


#<·
def filt_list(v: str) -> Result[list, FilterPropertyError]:
    # " [  ]" -> ''
    # '' -> falsy -> False -> Err
    pure_values: str = v.strip('[]').strip()

    if not pure_values:
        return Ok([])

    end_values: list[str] = []

    for value in pure_values.split(','):
        if ( val := filt_str(v=value.strip()) ).is_ok():
            end_values.append(val.value)
            continue

    return Ok(end_values)
