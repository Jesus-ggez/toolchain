import sys

#~>
from app.errors import TokenError


def is_empty_cmd() -> bool:
    return sys.argv == []


def get_raw_token() -> str:
    if is_empty_cmd():
        raise TokenError('Token<raw> not found: {sys.argv}')

    return sys.argv.pop(0)

