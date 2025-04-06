#~>
from .handler.prelude import SnippetMainHandler
from .metadata.mod import MetadataManager
from .creator.mod import CreatorManager
from .start.mod import StartManager
from .errors import SnippetError
from utils.result import Result
from .cmd import Terminal


class SnippetManager:
    def start(self) -> None: # Ok
        name: Result = Terminal.get_name()

        if name.is_err():
            raise name.error

        action: StartManager = StartManager(name.value)
        if ( err :=  action.check_error() ).is_err():
            raise err.error


    def new(self) -> None: # Ok
        metadata: MetadataManager = MetadataManager()
        if ( err := metadata.check_error() ).is_err():
            raise err.error

        metadata.create_meta()

        if ( err := metadata.check_error() ).is_err():
            raise err.error

        action: CreatorManager = CreatorManager(
            data=metadata.data,
        )
        if ( err := action.check_error() ).is_err():
            raise err.error


    def use(self, identifier: str) -> None: # ·here·
        if not identifier:
            raise SnippetError(
                message='Identifier must not be empty',
                call='SnippetManager.use',
                source=__name__,
            )

        alias: str = Terminal.get_alias()
        action: SnippetMainHandler = SnippetMainHandler(
            identifier=identifier,
            alias=alias,
        )
        if ( err := action.check_error() ).is_err():
            raise err.error
