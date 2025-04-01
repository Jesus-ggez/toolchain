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
                message='',
                filename='HandlerFactory',
                line=15,
            ))

        return Ok(data[name])
