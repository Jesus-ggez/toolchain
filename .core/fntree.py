class FnTree:
    def __init__(
        self,
        use_core: list = [],
        order: list = [],
        name: str = '',
    ) -> None:
        self._use_core: list = use_core
        self._order: list = order
        self._name: str = name


    def build(self) -> None:
        ...
