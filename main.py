import sys
from dotenv import load_dotenv

#~>
from utils.tokens import tokenize
from app.cmd import is_empty_cmd, get_raw_token
from app.struct import create_struct
from app.alias import use_alias


load_dotenv()


def main() -> None:
    sys.argv.pop(0)
    if is_empty_cmd():
        return

    if use_alias():
        return

    # main tree
    for argument in sys.argv:
        if argument.startswith('--'):
            break

        tokens: list[str] = tokenize(
            raw=get_raw_token(),
        )
        create_struct(tokens)


if __name__ == '__main__':
    main()
