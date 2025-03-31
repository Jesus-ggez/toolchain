class FactoryError(Exception):
    def __init__(self, filename: str, line: int, message: str) -> None:
        msg: str = f'{filename} | {line:^4} | {message}'
        super().__init__(msg)
