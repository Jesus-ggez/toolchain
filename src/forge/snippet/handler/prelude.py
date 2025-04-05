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

        actor: Result = HandlerFactory.get_factory(
            self._content._type,
        )
        if actor.is_err():
            self._use_error(actor)
            return

        action: Result = actor.value.build(
            self._content,
        )
        if action.is_err():
            self._use_error(action)
            return


    def get_content(self, v: str) -> Result[None, Exception]:
        if not v.isalnum():
            return Err(error=Exception(
                f'Invalid syntax: {v}'
            ))

        try:
            if len(v) <= 3:
                self._content: SnippetData = SnippetDb.find_by_id(
                    Identifier.to_number(v)
                )
                return Ok()

            self._content: SnippetData = SnippetDb.find_by_name(v)

        except Exception as e:
            return Err(error=e)
