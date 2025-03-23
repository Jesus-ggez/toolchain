#~>
from .managers.mod import get_manager
from src.core import FileManager
from .errors import SnippetError
from .cmd import Terminal
from utils.result import (
    Result,
    Err,
    Ok,
)


class SnippetManager:
    def create_manager(self) -> Result[None, SnippetError]:
        actor: FileManager = FileManager()
        content: list = []

        _value: Result =  Terminal().get_manager()
        if _value.is_ok():
            _new_content: Result = get_manager(name=_value.data)
            if _new_content.is_err():
                return Err(error=SnippetError(
                    message=f'create_manager | {_new_content.error}',
                    line=21,
                ))
            content.extend(_new_content.data)

        action: Result = actor.write.from_list(
            content=content,
            name='___.tc',
        )

        if action.is_err():
            print(action.error)
            return Err(error=action.error)

        return Ok()


