#~>
from .factories.errors import FactoryError
from .factories.base import Factory
from .factories.data import data
from utils.result import (
    Result,
    Err,
    Ok,
)


class HandlerFactory:
    @staticmethod
    def get_factory(name: str) -> Result[Factory, FactoryError]:
        if not (name in data):
            return Err(error=FactoryError(
                message=f'Invalid factory name: {name}',
                call='HandlerFactory.get_factory',
                source=__name__,
            ))

        return Ok(data[name])
