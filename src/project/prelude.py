#~>
from src.c_terminal.prelude import Terminal
from src.tcfmt.creator import TcFileCreator
from src.tcfmt.reader import TcFileReader


#.?
from .use.prelude import ProjectUseWorkspace
from .saver.prelude import ProjectSaver
from .constants import TcProjectConfig
from .errs import ProjectError


#<·
class ProjectManager:
    @staticmethod
    def start() -> None: # Ok
        terminal_content: Terminal = Terminal(field=TcProjectConfig.TEMPLATE_NAME)
        terminal_content.or_fail()

        TcFileCreator(
            tempname=terminal_content.value,
            root='project',
        ).or_fail()


    @staticmethod
    def new() -> None:
        data: TcFileReader = TcFileReader()
        data.add_filters(
            props=[
            'project-oficial-name',
            'entrypoints',
            'commands',
            'version',
            'target',
            'dotenv',
            'ignore',
            'langs',
            ]
        )
        data.or_fail()

        data.build()
        data.or_fail()

        last_record: ProjectSaver = ProjectSaver(metadata=data.value)
        last_record.or_fail()

        print('new project saved with id: ' + last_record.value)


    @staticmethod
    def use(identifier: str) -> None:
        if not identifier:
            raise ProjectError(
                message='Invalid identifier value',
                call='ProjectManager()',
                source=__name__,
            )

        terminal_content: Terminal = Terminal(field=TcProjectConfig.ALIAS)
        terminal_content.or_fail()

        record: ProjectUseWorkspace = ProjectUseWorkspace(
            alias=terminal_content.value,
            identifier=identifier,
        )
        record.or_fail()

        print(record.workspace_info)
