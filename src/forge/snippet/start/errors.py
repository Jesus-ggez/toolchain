class StartError(Exception):
    def __init__(self, message: str, filename: str) -> None:
        msg: str = f'{filename} | {message}'
        super().__init__(msg)


