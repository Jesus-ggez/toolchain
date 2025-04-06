class OperationError(Exception):
    def __init__(self, source: str, message: str, call: str) -> None:
        msg: str = f'{source} | {call} | {message}'
        super().__init__(msg)


class ScannerError(OperationError): ...

class TerminalError(OperationError): ...

class StartError(OperationError): ...
