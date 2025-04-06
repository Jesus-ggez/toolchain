#~>
from .factories.model import Factory
from .factories.data import data
from .errors import StartError
from utils.result import (
    Result,
    Err,
    Ok,
)


class StartManager:
    @staticmethod
    def get_factory(name: str) -> Result[Factory, StartError]:
        if not (name in data):
            return Err(error=StartError(
                call='StartManager.get_factory',
                message='Invalid tempname',
                source=__name__,
            ))

        factory: Factory = data[name]
        return Ok(factory)
