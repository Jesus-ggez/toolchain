#~>
from src.core.safe_cls import SafeClass
from src.core.errors import TcErr
from src.core.result import (
    Result,
    Err,
    Ok
)

#.?
from .data import data


#<·
class SKWFactory:
    @staticmethod
    def get_factory(key: str) -> Result[SafeClass, TcErr] | Result[None, TcErr]:
        if not key in data:
            return Err(error=TcErr(
                message='Invalid symbol key word: ' + key,
                call='SKWFactory.get_factory',
                source=__name__,
            ))

        return Ok(data[key])


