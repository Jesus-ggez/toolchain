from typing import NamedTuple


class Struct(NamedTuple):
    only_call: bool
    content: object
    use_core: bool
    use_params: bool
    params: dict = {}
    core: list = []
