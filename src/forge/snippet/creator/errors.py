class CreatorManagerError(Exception):
    def __init__(self, message: str, line: int, filename: str) -> None:
        msg: str = f'{filename} | {line:^4} | {message}'
        super().__init__(msg)

