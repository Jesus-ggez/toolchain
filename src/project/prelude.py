#~>
from src.c_terminal.prelude import Terminal
from src.tcfmt.creator import TcFileCreator
from src.tcfmt.reader import TcFileReader


#.?
from .use.workspace import ProjectUseWorkspace
from .constants import TcProjectConfig
from .new.saver import ProjectSaver
from .errs import ProjectError


#<·
class ProjectManager:
    @staticmethod
    def start() -> None: # Ok
        terminal_content: Terminal = Terminal(field=TcProjectConfig.TEMPLATE_NAME)

        terminal_content.ensure_ok()

        action: TcFileCreator = TcFileCreator(
            tempname=terminal_content.value,
            root='project',
        )
        action.ensure_ok()


    @staticmethod
    def new() -> None:
        tc_reader: TcFileReader = TcFileReader()

        if ( err := tc_reader.add_filters(props=TcProjectConfig.FILTERS) ).is_err():
            raise err.error

        tc_reader.build()
        tc_reader.ensure_ok()

        project_content: ProjectSaver = ProjectSaver(metadata=tc_reader.value)
        project_content.ensure_ok()

        print(project_content.value)


    @staticmethod
    def use(identifier: str) -> None:
        if not identifier:
            raise ProjectError(
                message='Invalid identifier',
                call='ProjectManager.use',
                source=__name__,
            )

        terminal_content: Terminal = Terminal(field=TcProjectConfig.ALIAS)
        terminal_content.ensure_ok()

        action: ProjectUseWorkspace = ProjectUseWorkspace(
            alias=terminal_content.value,
            identifier=identifier,
        )

        action.ensure_ok()

        print('Project created successfully')
