# main
class SnippetError(Exception):
    def __init__(self, line: int, message: str) -> None:
        msg: str = f'{line:^4} | {message}'
        super().__init__(msg)


class TerminalError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class SnippetMetaError(SnippetError):
    def __init__(self, line: int, message: str) -> None:
        super().__init__(line, message)




# derive
class SnippetMetaImplError(SnippetMetaError):
    def __init__(self, line: int, message: str, _err) -> None:
        print(_err)
        super().__init__(line, message)
