class Rules:
    def __setattr__(self, name: str, value) -> None:
        raise ValueError('Inmutable arg')



class ForgeRules(Rules):
    ...
