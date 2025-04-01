class FactoryError(Exception):
    def __init__(self, message: str, filename: str, line: int) -> None:
        msg: str = f''

        super().__init__(msg)
