import sys
from dotenv import load_dotenv

#~>
from utils.terminal import is_empty_cmd, get_next_arg
from app_v1.struct import create_struct
from utils.tokens import tokenize
from utils.result import Result



load_dotenv()


def main() -> None:
    sys.argv.pop(0)

    if is_empty_cmd():
        return

    #if use_alias():
    #    return

    global_context: dict = {
        'num_token': 0,
    }
    identifier: int = global_context['num_token']

    # main tree
    for _ in sys.argv:
        global_context[identifier] = {}

        _raw_token: Result = get_next_arg()
        if _raw_token.is_err():
            print(_raw_token)
            return

        raw_token: str = _raw_token.data
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
            return
        global_context['num_token'] += 1


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'__main__ | {e}')



