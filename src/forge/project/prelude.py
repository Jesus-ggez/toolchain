#~>
from .creator import CreatorManager
from .start import StartManager
from utils.result import Result
from .cmd import Terminal


class ProjectManager:
    def start(self) -> None:
        name: Result = Terminal.get_name()
        if name.is_err():
            raise name.error

        actor: Result = StartManager.get_factory(name.value)
        if actor.is_err():
            raise actor.error

        action: Result = actor.value.build()
        if action.is_err():
            raise action.error


    def new(self) -> None:
        actor: CreatorManager = CreatorManager()
        if ( err := actor.check_error() ).is_err():
            raise err.error


    def use(self) -> None: ...
