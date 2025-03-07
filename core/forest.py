from forge import ForgeTree
# from core import CoreTree

class CoreTree:
    def __init__(self, foo: list) -> None:
        raise NotImplementedError()


class ForceTree(CoreTree):
    ...

forest: dict = {
    '!': ForgeTree,
    ':': CoreTree,
    '·': ForceTree,
}
