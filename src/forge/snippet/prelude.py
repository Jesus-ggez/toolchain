#~>
from .metadata.errors import SnippetMetadataError
from .metadata.mod import SnippetMetadata
from .start.mod import StartManager
from .errors import SnippetError
from .cmd import Terminal
from utils.result import (
    Result,
)


class SnippetManager:
    def start(self) -> None:
        name: str = self.__class__.__name__
        temp_name: Result = Terminal.get_tempname()
        if temp_name.is_err():
            raise SnippetError(
                message='The argument are not valid for a starter template',
                filename=name,
                line=15,
            )

        action: Result = StartManager.build(template=temp_name.data)
        if action.is_err():
            raise SnippetError(
                message='Error building startup configuration',
                filename=name,
                line=23,
            )


    def build(self) -> None:
        name: str = self.__class__.__name__
        file: dict = {}
        metadata: SnippetMetadata = SnippetMetadata(
            context=file,
        )
        if metadata.check_error().is_err():
            raise metadata.check_error().error

        get_metadata: Result = metadata.generate()
        if get_metadata.is_err():
            raise SnippetMetadataError(
                message=f'Fields not found: {get_metadata.error}',
                filename=name,
                line=39,
            )


    def use(self) -> None:
        ...
