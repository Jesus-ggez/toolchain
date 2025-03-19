#~>
from app.context import CreateContext
from app.data import forest


def create_struct(tokens: list[str], context: dict) -> None:
    context.update(
        {
            'node_pointer': forest,
            'action': False,
            'init': True,
            'args': [],
        }
    )
    for token in tokens:
        CreateContext(
            context=context,
            token=token,
        )
