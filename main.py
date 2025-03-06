import sys

#~
from core import Root, forest
from app import core_fn, tool_fn

def main() -> None:
    data: list[str] = sys.argv
    data.pop(0)

    # ['a', 'b', 'c', ...]

    for cmd in data:
        tree: str = cmd[0]

        if tree.isalnum():
            Root(cmd)
            continue

        use: object | None = forest.get(tree)

        if use is None:
            raise ValueError('Invalid Syntax')

        use(cmd.removeprefix(tree))









if __name__ == '__main__':
    main()
