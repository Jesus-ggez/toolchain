#~>
from src.core.result import (
    Result,
    Err,
    Ok,
)


#.?
from .errs import ParserError


#<·
def parse_to_string(v: str) -> Result[str, ParserError]:
    if not v.endswith('"') or not v.startswith('"'):
        return Err(error=ParserError(
            message='Invalid value to parse',
            call='parse_to_string()',
            source=__name__,
        ))

    if not v[1:-1].strip():
        return Err(error=ParserError(
            message='Invalid null to parse',
            call='parse_to_string()',
            source=__name__,
        ))

    return Ok(v[1:-1].strip())
