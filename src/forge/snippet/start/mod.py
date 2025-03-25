#~>
from utils.result import (
    Result,
    Err,
    Ok,
)


class StartManager:
    @staticmethod
    def build(template: str) -> Result[None, Exception]:
        return Err(
            Exception()
        )
