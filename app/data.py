#~>
from src.py_utils import data as pydata
from src.snippet import data as sdata
from src.project import data as pdata


#<·
def print_ok(): print('Ok')
def print_ok_with_args(*args): print(*args)

forest: dict = {
    'snippet': sdata,
    'project': pdata,
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
forest.update(pydata)

