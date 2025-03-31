#~>
from .errors import FactoryError
from .base import Factory
from utils.result import (
    Result,
    Err,
    Ok,
)


class BasicFactory(Factory):
    def __init__(self, raw: dict) -> None:
        super().__init__(raw)
        data: Result = self.build(token=self.token_name)

        if data.is_err():
            self._use_error(data)
            return

        if len(data.value) < 3:
            self._use_error(Err(error=FactoryError(
                message='Invalid syntax',
                filename=self.name,
                line=21
            )))

        self._raw[self.token_name] = data.value[2].replace("'", "")
