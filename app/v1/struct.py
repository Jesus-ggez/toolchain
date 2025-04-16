#~>
from app.v1.context import ContextManager
from app.v1.data import forest
from utils.result import (
    Result,
    Err,
    Ok,
)


def create_struct(tokens: list[str], context: dict) -> Result[None, Exception]:
    context.update(
        {
            'node_pointer': forest,
            'handler': None,
            'init': True,
            'args': [],
        }
    )

    if tokens[0].replace('_', 's').isalnum():
        tokens.insert(0, ':')

    for token in tokens:
        action: ContextManager = ContextManager(
            context=context,
            token=token,
        )

        if ( err := action.check_error() ).is_err():
            return err

    return Ok()
