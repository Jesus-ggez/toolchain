class BaseError(Exception):
    def __init__(self, source: str, call: str, message: str) -> None:
        msg: str = f'{source} | {call} | {message}'
        super().__init__(msg)

class TerminalError(BaseError): ...

class SnippetError(BaseError): ...

