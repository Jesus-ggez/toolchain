class StartError(Exception):
    def __init__(self, message: str, source: str, call: str) -> None:
        msg: str = f'{source} | {call} | {message}'
        super().__init__(msg)


