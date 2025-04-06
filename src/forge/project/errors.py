class OperationError(Exception):
    def __init__(self, filename: str, message: str) -> None:
        msg: str = f'{filename} | {message}'
        super().__init__(msg)


class ScannerError(OperationError): ...

class TerminalError(OperationError): ...

class StartError(OperationError): ...
