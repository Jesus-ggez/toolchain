#~>
from src.core import FileManager
from .base import Factory
from utils.result import (
    Result,
    Err,
    Ok,
)


class Simple(Factory):
    def __init__(self) -> None:
        super().__init__()
        self._type('simple')


    def build(self, content) -> Result[None, Exception]:
        self._ctt = content

        meta: Result = self.create_from_metadata()
        if meta.is_err():
            return meta

        action: Result = FileManager().write.from_str(
            content=self.file_content,
            name=self.filename,
        )

        if action.is_err():
            return action

        return Ok()

    def create_from_metadata(self) -> Result[None, Exception]:
        raw_data = self._ctt.content.split('<~>')

        if len(raw_data) != 2:
            return Err(error=Exception(
                'Hasnt basic data',
            ))

        self.file_content: str = raw_data[1]
        self.filename: str = self._ctt.name + '.' + self.generate_meta(
            metadata=raw_data[0].strip(),
        ).get('lang', '.txt')

        return Ok()


    def generate_meta(self, metadata: str) -> dict:
        meta: dict = {}
        for item in metadata.split(';'):
            if not ('.' in item):
                continue

            key, *rest = item.split('.', maxsplit=1)

            value = rest[0] if rest else ''
            meta.update(
                {
                    key: value
                }
            )

        return meta
