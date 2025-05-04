#~>
from .errs import PropertyError
from src.core.result import (
    Result,
    Err,
    Ok
)


#<·
def get_property(item: str, name: str) -> Result[str, PropertyError]:
    if not item.startswith(name):
        return Err(error=PropertyError(
            message='Property not found',
            call='fn::get_property',
            source=__name__,
        ))

    parts: list[str] = item.split(sep='=')

    if len(parts) != 2:
        return Err(error=PropertyError(
            message='Invalid Property fmt',
            call='fn::get_property',
            source=__name__,
        ))

    return Ok(parts[1].strip().replace('"', ''))
