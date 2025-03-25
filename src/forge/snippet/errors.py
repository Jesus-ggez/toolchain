class SnippetError(Exception):
    def __init__(self, message: str, line: int, filename: str) -> None:
        msg: str = f'{filename} | {line:^4} | {message}'
        super().__init__(msg)


class TerminalError(Exception):
    def __init__(self, message: str) -> None:
        msg: str = f'{message} | '
        super().__init__(msg)

