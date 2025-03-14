try:
    from .tree import (
        main_token_type,
        Context,
    )
    from .forge import data

except ImportError:
    from tree import (
        main_token_type,
        Context,
    )
    from forge import data


class CreateContext:
    def __init__(self, token: str, context: Context) -> None:
        if not token:
            raise ValueError('Invalid Token')

        self.__context: Context = context
        self.__token: str = token

        # init
        self.build()


    def build(self) -> None:
        token_type: str = main_token_type.get(self.__token, 'node_name')




















