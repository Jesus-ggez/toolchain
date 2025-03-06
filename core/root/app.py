from abstract.itree import Tree
from core import forest


class RootTree(Tree):
    def __init__(self, cmd: str) -> None:
        if not cmd:
            raise ValueError('Not found args')

        self._cmd: str = cmd
        self.pre_data: list = []


        # process
        if self.redirect():
            return

        self.pre_process()

    def redirect(self) -> bool:
        begin: str = self._cmd[0]
        tree= forest.get(begin)
        exists_tree: bool = not (tree is None)

        if exists_tree:
            tree(self._cmd)

        return exists_tree


    def pre_process(self) -> None:
        abc: str = ''
        symbol: str = ''

        for character in self._cmd:
            if character.isalnum() or character == '_':
                abc += character
                continue

            symbol += character




    def tokenize(self) -> None:
        ...

    def to_tasm(self) -> None:
        ...

    def executor(self) -> None:
        ...
