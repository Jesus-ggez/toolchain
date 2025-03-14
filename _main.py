import sys

#~>
from utils.tokens import tokenize
from src import forest


def main() -> None:
    # don't touch
    data: list[str] = sys.argv
    data.pop(0)
    if not data: return

    # content
    flag: str = data.pop(0)
    tree: dict | None = forest.get(flag)

    if tree is None:
        raise ValueError('Tree not found')

    tree(data)

if __name__ == '__main__':
    main()
