#<~
from snippet_db import (
    SnippetData,
    Identifier,
    SnippetDb,
)


#~>
from src.utils.base_safe import SafeClass
from .errors import HandlerError
from .app import HandlerFactory
from utils.result import (
    Result,
    Err,
    Ok,
)


class SnippetMainHandler(SafeClass):
    def __init__(self, identifier: str, alias: str) -> None:
        super().__init__()

        content: Result = self.get_content(identifier)
        if content.is_err():
            self._use_error(content)
            return

        if alias:
            old: dict = self._content.to_dict()
            old['name'] = alias
            self._content = SnippetData(
                **old
            )

        actor: Result = HandlerFactory.get_factory(
            name=self._content._type,
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


    def get_content(self, v: str) -> Result[None, HandlerError]:
        if not v.isalnum():
            return Err(error=HandlerError(
                call='SnippetMainHandler.get_content',
                message=f'Invalid syntax: {v}',
                source=__name__,
            ))

        try:
            if len(v) <= 3:
                self._content: SnippetData = SnippetDb.find_by_id(
                    Identifier.to_number(v)
                )
                return Ok()

            self._content: SnippetData = SnippetDb.find_by_name(v)
            return Ok()

        except Exception as e:
            return Err(error=e)
