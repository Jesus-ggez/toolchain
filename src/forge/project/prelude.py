#~>
from .errors import ProjectError
from .start import StartProject
from utils.result import Result
from .new import NewProject
from .use import UseProject
from .cmd import Terminal


class ProjectManager:
    def start(self) -> None:
        name: Result = Terminal.get_name()
        if name.is_err():
            raise name.error

        actor: StartProject = StartProject(
            name=name.value,
        )
        if ( err := actor.check_error() ).is_err():
            raise err.error

        action: Result = actor.build()
        if action.is_err():
            raise action.error


    def new(self) -> None:
        actor: NewProject = NewProject()
        if ( err := actor.check_error() ).is_err():
            raise err.error

        action: Result = actor.build()
        if action.is_err():
            raise action.error


    def use(self, identifier: str) -> None:
        if not identifier:
            raise ProjectError(
                message='Invalid identifier',
                call='ProjectManager.use',
                source=__name__,
            )

        alias: str = Terminal.get_alias()
        action: UseProject = UseProject(
            identifier=identifier,
            alias=alias,
        )
        if ( err := action.check_error() ).is_err():
            raise err.error
