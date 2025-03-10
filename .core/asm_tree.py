def asm_tree(raw: list[str], rules: dict[str, type]) -> None:
    data: list = []

    for item in raw:
        if item.isalnum():
            data.append(item)
            continue

        action: type | None = rules.get(item)

        if action is None:
            raise ValueError('Invalid Argument')

        action(*data)
        data.clear()
