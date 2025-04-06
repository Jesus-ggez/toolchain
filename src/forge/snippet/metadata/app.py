#~>
from .factories.errors import FactoryError
from .factories.base import Factory
from .factories.data import data
from utils.result import (
    Result,
    Err,
    Ok,
)


class MetaFactory:
    @staticmethod
    def get_factory(token: str) -> Result[Factory, FactoryError]:
        if not (token in data):
            print(token in data)
            return Err(error=FactoryError(
                message='Invalid struct of document',
                call='MetaFactory.get_factory',
                source=__name__,
            ))

        return Ok(data[token])
