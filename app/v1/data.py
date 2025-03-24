#~>
from src.forge import data as fdata
from src.core import data as cdata


def print_ok(): print('Ok')
def print_ok_with_args(*args): print(*args)

forest: dict = {
    'forge': fdata,
    'core': cdata,
    }

test: dict = {
    'test_fn': print_ok,
    'test': {
        'ok': print,
        'branch': {
            'ok': print_ok_with_args
        }
    }
}

#forest.update(test)


