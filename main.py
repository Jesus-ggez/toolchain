import sys
from dotenv import load_dotenv

#~>
from utils.terminal import is_empty_cmd, get_next_arg
from app.struct import create_struct
#from app.v1.alias import use_alias
from utils.errors import safe_exec
from utils.tokens import tokenize
from src.core.result import Result


load_dotenv()


@safe_exec
def main() -> None:
    get_next_arg() # del "main.py" from arguments = []

    if is_empty_cmd():
        return

    """
    if ( alias := use_alias() ):
        print(alias.error or alias.data)
        return
    """

    global_context: dict = {
        'num_token': 0,
    }
    identifier: int = global_context['num_token']

    # main tree
    for _ in sys.argv:
        global_context[identifier] = {}

        _raw_token: Result = get_next_arg()
        if _raw_token.is_err():
            return

        raw_token: str = _raw_token.value
        if raw_token.startswith('--'):
            break

        tokens: list[str] = tokenize(
            raw=raw_token,
        )

        # ._.
        action: Result = create_struct(
            context=global_context[identifier],
            tokens=tokens,
        )
        if action.is_err():
            print(action.error)
            return

        global_context['num_token'] += 1


if __name__ == '__main__':
    init: Result = main()

    if init.is_err():
        print(f'python: {init}')
