from utils.result import (
    Result,
    Err,
    Ok,
)


class Error(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

