from typing import NamedTuple


class Token(NamedTuple):
    expected: set
    name: str

main_token_type: dict = { #·>
    ':': Token(
        expected={'node_name'},
        name='move_to',
    ),
    '<·': Token(
        expected={'node_name', 'only_call'},
        name='use_core',
    ),
    '()': Token(
        expected={'core_tool'},
        name='only_call',
    )
}


