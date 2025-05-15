#~>
from src.core.result import (
    Result,
    Ok,
)


#.?
from .context import ContextManager
from .data import forest


#<·
def create_struct(tokens: list[str]) -> Result[None, Exception]:
    context: dict = {
        'node_pointer': forest,
        'handler': None,
        'init': True,
        'args': [],
    }

    if tokens[0].replace('_', 'z').isalnum():
        tokens.insert(0, ':')

    for token in tokens:
        action: ContextManager = ContextManager(
            context=context,
            token=token,
        )

        if ( err := action.check_error() ).is_err():
            return err

    return Ok()
