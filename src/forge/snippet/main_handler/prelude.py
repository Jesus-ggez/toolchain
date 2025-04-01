#<~
from snippet_db import (
    SnippetData,
    Identifier,
    SnippetDb,
)


#~>
from src.utils.base_safe import SafeClass
from .app import HandlerFactory
from utils.result import (
    Result,
    Err,
    Ok,
)


class SnippetMainHandler(SafeClass):
    def __init__(self, identifier: str) -> None:
        super().__init__()

        content: Result = self.get_content(identifier)
        if content.is_err():
            self._use_error(content)
            return

        actor: Result = HandlerFactory.get_factory(content.value._type)
        if actor.is_err():
            self._use_error(actor)
            return

        action: Result = actor.value(content)
        if action.is_err():
            self._use_error(action)
            return


    def get_content(self, v: str) -> Result[None, Exception]:
        actor = SnippetDb.find_by_name

        if len(v) <= 2:
            actor = SnippetDb.find_by_id
            v = Identifier.to_number(v)

        try:
            self._content: SnippetData = actor(v)
            return Ok()

        except Exception as e:
            return Err(error=e)
