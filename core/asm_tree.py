def create_rule(value: str) -> None:
    ...


def asm_tree(raw: list[str], rules: dict) -> None:
    """
    add in raw[0] a base instruction if not exists
    """
    data: list = []

