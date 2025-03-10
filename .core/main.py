import sys

#~>
from app import tokenize
from core.forest import forest, CoreTree


def main() -> None:
    data: list[str] = sys.argv
    data.pop(0) # remove <main.py>

    for command in data:
        raw: list[str] = tokenize(command) # ['!', 'cmd_name', ]
        if not raw: continue

        tree: object | None = forest.get(raw[0])

        if tree is None:
            CoreTree(raw)
            continue

        tree(raw[1:])




if __name__ == '__main__':
    main()
