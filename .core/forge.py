try:
    from asm_tree import asm_tree

except:
    from .asm_tree import asm_tree


class ForgeTree:
    def __init__(self, cmd: list) -> None:
        self.__cmd: list = cmd
        self._rules: dict = {
        }

    def create_asm_tree(self) -> None:
        asm_tree(self.__cmd, self._rules)



