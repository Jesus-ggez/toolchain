class FactoryError(Exception):
    def __init__(self, source: str, call: str, message: str) -> None:
        msg: str = f'···> {source} \n| {call} \n| {message}'
        super().__init__(msg)
