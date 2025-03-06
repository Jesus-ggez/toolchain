class SnippetRules:
    def __setattr__(self, name: str, value) -> None:
        raise ValueError('Inmutable arg')


    VERSION: str = '#·v'
    IGNORE: str = '#···'
    TYPE: str = '#<<<'
