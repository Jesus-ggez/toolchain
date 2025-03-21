from sys import argv as arguments

#~>

def is_empty_cmd() -> bool:
    return not arguments


def get_next_arg() -> str:
    if is_empty_cmd():
        raise ValueError('Not found arguments')

    return arguments.pop(0)


def get_copy_next_arg() -> str:
    if is_empty_cmd():
        raise ValueError('Not found arguments')

    return arguments[0]
