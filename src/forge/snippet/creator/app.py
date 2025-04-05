#<~
from snippet_db import SnippetDb


#~>
from src.utils.base_safe import SafeClass
from utils.result import (
    Result,
    Err,
    Ok,
)


class SnippetCreator(SafeClass):
    def __init__(self, content: dict, db = SnippetDb) -> None:
        self._content: dict = content
        self._db = db

        super().__init__()
        self._params: tuple = (
            'lang',
        )

        self.__add_metadata()

        action: Result = self.__save()
        if action.is_err():
            self._use_error(action)
            return


    def __save(self) -> Result[None, Exception]:
        try:
            self._db.add_in(
                name=self._content['name'],
                version=self._content['version'],
                content=''.join(self._content['target']),
                _type=self._content['type'],
            )

            return Ok()

        except Exception as e:
            return Err(error=e)


    def __add_metadata(self) -> None:
        if not ('lang' in self._content):
            return

        # magic! str
        new_line = lambda key: f'{key}.' + self._content[key] + ';'

        custom: list = [new_line(key=key) for key in self._params]
        custom.append('<~>')
        _original: list = self._content['target']

        self._content['target'] = custom + _original

