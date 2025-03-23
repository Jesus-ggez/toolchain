#~>
from .factories.base_factory import TokenFactory
from .factories.data import all_data
from .errors import TokenError
from utils.result import (
    Result,
    Err,
    Ok,
)


class ActionsFactory:
    @staticmethod
    def get_factory(name: str) -> Result[TokenFactory, TokenError]:
        factory = all_data.get(name)

        if not factory:
            return Err(error=TokenError(
                message='Token not found',
                filename=__name__,
                token=name,
                line=17,
            ))

        return Ok(factory)

