#~>
from .start.mod import StartManager
from .terminal import Terminal
from utils.result import Result


class ProjectManager:
    def start(self) -> None:
        name: Result = Terminal.get_name()

        if name.is_err():
            raise name.error

        action: StartManager = StartManager(name.value)
        if ( err :=  action.check_error() ).is_err():
            raise err.error


    def new(self) -> None: ...
    def use(self) -> None: ...
