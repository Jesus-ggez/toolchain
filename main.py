import sys

#~>
from utils.tokens import tokenize
from forest.mod import forest


def main() -> None:
    data: list[str] = sys.argv
    data.pop(0)

    if data[0].startswith('--'):
        raise NotImplementedError('flags implemented in the future. --foo')


    for item in data:
        cmd: list[str] = tokenize(
            raw=item,
        )
        tree_objective: str = cmd.pop(0)

        tree: type | None = forest.get(tree_objective)

        if tree is None:
            print(f'Tree not found: {tree_objective}')
            continue

        tree.values = item
        tree.call_branch()


if __name__ == '__main__':
    main()
