class SnippetMetadataError(Exception):
    def __init__(self, message: str, filename: str, line: int) -> None:
        msg: str = f'{filename} | {line:^4} | {message}'
        super().__init__(msg)
