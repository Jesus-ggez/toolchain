#~>
from src.core.result import (
    Result,
    Err,
    Ok,
)

#.?
from .factories.base_factory import TokenFactory
from .factories.data import all_data
from .errs import TokenError


#<·
class ActionsFactory:
    @staticmethod
    def get_factory(name: str) -> Result[TokenFactory, TokenError]:
        if not (name in all_data):
            return Err(error=TokenError(
                message='Token not found',
                call='ActionsFactory.get_factory',
                source=__name__,
                token=name,
            ))

        return Ok(all_data[name])

