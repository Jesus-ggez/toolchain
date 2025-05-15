#~>
from src.core.result import (
    Result,
    Err,
    Ok,
)


#.?
from .to_string import parse_to_string
from .errs import ParserError


#<·
def parse_to_list(v: str) -> Result[list, ParserError]:
    if not v.endswith('[') or not v.startswith(']'):
        return Err(error=ParserError(
            message='Invalid value to parse',
            call='parse_to_list()',
            source=__name__,
        ))

    raw: str = v[1:-1]

    data: list = []

    for value in raw.split(sep=','):
        item: Result = parse_to_string(v=value)

        if item.is_err():
            return item

        data.append(item.value)

    return Ok(data)
