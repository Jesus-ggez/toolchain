#~>
from app.context import CreateContext
from app.data import forest


def create_struct(tokens: list[str]) -> None:
    context: dict = {
        'pointer': forest,
        'action': False,
        'init': True,
        'args': [],
    }
    for token in tokens:
        CreateContext(
            context=context,
            token=token,
        )
