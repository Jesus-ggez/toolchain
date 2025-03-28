class TerminalError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class SnippetError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
