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
                filename=__name__,
                message='Invalid tempname',
            ))

        factory: Factory = data[name]
        return Ok(factory)
