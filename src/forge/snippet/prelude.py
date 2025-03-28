#~>
from .main_handler.prelude import SnippetMainHandler
from .metadata.mod import MetadataManager
from .creator.mod import CreatorManager
from .start.mod import StartManager
from .errors import SnippetError
from utils.result import Result
from .cmd import Terminal


class SnippetManager:
    def start(self) -> None:
        name: Result = Terminal.get_name()

        if name.is_err():
            raise name.error

        action: StartManager = StartManager(name.data)
        if action.check_error().is_err():
            raise action.check_error().error


    def new(self) -> None:
        context: dict = {}
        metadata: MetadataManager = MetadataManager(
            context=context,
        )
        if metadata.check_error().is_err():
            raise metadata.check_error().error

        action: CreatorManager = CreatorManager(
            data=metadata,
        )
        if action.check_error().is_err():
            raise action.check_error().error


    def use(self, identifier: str) -> None:
        if not identifier:
            raise SnippetError(
                'Identifier must not be empty'
            )

        action: SnippetMainHandler = SnippetMainHandler(
            identifier=identifier,
        )
        if action.check_error().is_err():
            raise action.check_error().error
