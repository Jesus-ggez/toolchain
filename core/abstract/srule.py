class Rule:
    def __setattr__(self, name: str, value) -> None:
        raise ValueError('Inmutable property')

