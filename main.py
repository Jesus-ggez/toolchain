"""
use -> python ~/toolchain/main.py
"""
from dotenv import load_dotenv

#~>
from utils.terminal import is_empty_cmd, get_next_arg
from utils.tokens import tokenize

from nucleus.constants import TcGlobalContext
from app.struct import create_struct

from src.core.errors import safe_exec
from src.core.result import Result


#<·
load_dotenv()


@safe_exec
def main() -> None:
    """ run ALL"""
    get_next_arg() # del "main.py" from arguments = []

    if is_empty_cmd():
        return

    context: Result = get_next_arg()
    if context.is_err():
        return

    TcGlobalContext()

    tokens: list[str] = tokenize(raw=context.value)

    action: Result = create_struct(
        tokens=tokens,
    )
    if action.is_err():
        print(action.error)
        return

    return


if __name__ == '__main__':
    init: Result = main()

    if init.is_err():
        print(f'python: {init}')
