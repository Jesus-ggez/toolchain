import json

#<~
from snippet_db import (
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
            self._content['name'] = alias

        actor: Result = HandlerFactory.get_factory(
            name=self._content['type_']
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
        try:
            if len(v) <= 3 and v.isalnum():
                v = '00' + v
                raw: str = SnippetDb.find_by_id(
                    Identifier.to_number(v[-3:])
                )
                self._content: dict = json.loads(raw)
                return Ok()

            raw: str = SnippetDb.find_by_name(v)
            self._content: dict = json.loads(raw)
            return Ok()

            """
            return Err(error=HandlerError(
                call='SnippetMainHandler.get_content',
                message=f'Invalid syntax: {v}',
                source=__name__,
            ))
            #"""

        except Exception as e:
            return Err(error=e)

