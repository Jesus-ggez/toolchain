#~>
from app.errors import ContextError


def modify_context(argument: str, context: dict) -> None:
    values: list = argument.split(sep='::')
    if len(values) != 2:
        raise ContextError('Context config token error')

    context[values[0]] = values[1]
