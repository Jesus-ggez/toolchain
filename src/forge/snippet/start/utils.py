#~>
from .data import data


def print_help() -> None:
    t: str = '  '
    print('commands:')
    for d in data:
        print(t + d)
