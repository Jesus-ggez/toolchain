#~>
from src.utils.base_safe import SafeClass
from .errors import FactoryError
from utils.result import (
    Result,
    Err,
    Ok,
)


class Factory(SafeClass):
    def __init__(self) -> None:
        super().__init__()
        self.divider: str = '<~>'


    def _use_type(self, v: str) -> None:
        self.type: str = v


    def build(self, content: dict) -> Result[None, Exception]:
        return Err(error=FactoryError(
            message='Not implemented',
            call='Factory.build',
            source=__name__,
        ))


    def __generate_meta(self, raw_metadata: str) -> dict:
        meta: dict = {}
        for item in raw_metadata.split(sep=';'):
            if not ('.' in item):
                continue

            key, *rest = item.split(sep='.', maxsplit=1)

            value: str = rest[0] if rest else ''

            meta.update(
                {
                    key: value,
                }
            )

        return meta


    def create_metadata(self, content) -> Result[None, Exception]:
        base_data: list = content['content'].split(self.divider)
        if len(base_data) != 2:
            return Err(error=FactoryError(
                call='Factory.create_metadata',
                message='hasnt basic data',
                source=__name__,
            ))

        self.file_content: str = base_data[1]

        self.metadata: dict = self.__generate_meta(
            raw_metadata=base_data[0].strip(),
        )

        return Ok()
