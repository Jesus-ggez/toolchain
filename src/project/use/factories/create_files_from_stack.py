from typing import Any
import json


#¿?
from snippet_db import Identifier
from project_db import SnippetDb


#~>
from src.core.safe_cls import SafeClass
from src.core.file_utils import Writer
from src.core.errors import safe_exec
from src.core.result import (
    Result,
    Ok,
)


#.?
from .errs import TcErr


#<·
class CreateFilesFromStack(SafeClass):
    def __init__(self, context: dict) -> None:
        super().__init__()

        self._context: dict = context
        self.__build()

        context['stack'].clear()


    def __build(self) -> None:
        # return print('usando stack')

        if ( err := self.__create_all_files() ).is_err():
            return self._use_error(err)


    def __create_all_files(self) -> Result[None, TcErr]:
        self._context['stack'].append(
            self._context['last_token']
        )

        for item in self._context['stack']:
            data: Result = self.___get_data(raw_iden=item)

            if data.is_err():
                return data

            snippet: dict = data.value
            action: Result = Writer.from_str(
                content=snippet['content'],
                name=snippet['name'],
            )

            if action.is_err():
                return action

        return Ok()


    @safe_exec
    def ___get_data(self, raw_iden: str) -> Any:
        iden: int = Identifier.to_number(raw_iden)

        res: str = SnippetDb.get_snippet(iden)
        if not res:
            raise ValueError('Snippet not found')

        return json.loads(res)
