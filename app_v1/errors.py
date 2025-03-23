class ContextError(Exception):
    def __init__(self, message: str, line: int, filename: str) -> None:
        msg: str = f'{filename} | {line:^4} | {message} '
        super().__init__(msg)


class TokenError(ContextError):
    def __init__(self, message: str, line: int, filename: str, token: str) -> None:
        super().__init__(
            message=message + f' | token: {token}',
            filename=filename,
            line=line,
        )


class TreeError(ContextError):
    def __init__(self, message: str, line: int, filename: str) -> None:
        super().__init__(message, line, filename)
