import sys
from dotenv import load_dotenv

#~>
from utils.tokens import tokenize
from app.cmd import is_empty_cmd, get_raw_token
from app.mod_context import modify_context
from app.struct import create_struct
from app.alias import use_alias



load_dotenv()


def main() -> None:
    sys.argv.pop(0)

    if is_empty_cmd():
        return

    if use_alias():
        return

    global_context: dict = {
        'num_token': 0,
    }
    identifier: int = global_context['num_token']

    # main tree
    for argument in sys.argv:
        global_context[identifier] = {}

        if argument.startswith('·-'):
            argument.removeprefix('·-')
            modify_context(
                context=global_context[identifier],
                argument=argument,
            )
            continue

        _raw_token: str =  get_raw_token()
        if _raw_token.startswith('--'):
            break


        tokens: list[str] = tokenize(
            raw=_raw_token,
        )
        create_struct(
            context=global_context[identifier],
            tokens=tokens,
        )
        global_context['num_token'] += 1


if __name__ == '__main__':
    main()





