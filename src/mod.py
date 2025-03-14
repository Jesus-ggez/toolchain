from utils.tokens import tokenize

#~>
from .tree import (
    #BuildContext,
    Context,
)


class Tree:
    def __init__(self, wood: dict) -> None:
        self.__wood: dict = wood


    def build(self, cmd_line: str) -> None:
        self.tokens: list = tokenize(cmd_line)

        self.context:  Context = Context()
        self.context.actual_tpos = self.__wood

        for token in self.tokens:
            ...
            #BuildContext(token)
