import sys
from dotenv import load_dotenv

#~>
from src.forge import data as fdata
from src.core import data as cdata


load_dotenv()

forest: dict = {
    'core': cdata,
    'forge': fdata,
}


def get_argv() -> str:
    if sys.argv:
        return sys.argv.pop(0)

    raise ValueError('Args not found')


def use_dict(data: dict, value: str, msg: str) -> dict:
    _data = data.get(value)
    if _data is None:
        raise ValueError(msg)
    return _data


def main() -> None:
    sys.argv.pop(0)

    _tree: str = get_argv()
    tree_name, action = _tree.split(':')

    tree: dict = use_dict(
        msg=f'Tree not found: {tree_name}',
        value=tree_name,
        data=forest,
    )

    branch: dict = tree
    if action != '?':
        branch: dict = use_dict(
            msg=f'Action not found: {action}',
            value=action,
            data=tree,
        )

    _fn_line: str = get_argv()
    fn_name, values = _fn_line.split('.')

    fn = branch.get(fn_name)
    if fn is None:
        raise ValueError('Invalid Action')

    if values == '->':
        fn(get_argv())
        return

    if not values:
        fn()
        return

    fn(*values.split(','))


if __name__ == '__main__':
    main()
