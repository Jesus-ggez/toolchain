#~>
from src.c_terminal.prelude import Terminal
from src.tcfmt.creator import TcFileCreator
from src.tcfmt.reader import TcFileReader


#.?
from .logic_struct_files.project_saver import ProjectSaver
from .constants import TcProjectConfig


#<·
class ProjectManager:
    @staticmethod
    def start() -> None: # Ok
        terminal_content: Terminal = Terminal(field=TcProjectConfig.TEMPLATE_NAME)

        if ( err := terminal_content.check_error() ).is_err():
            raise err.error

        action: TcFileCreator = TcFileCreator(
            tempname=terminal_content.value,
            root='project',
        )

        if ( err := action.check_error() ).is_err():
            raise err.error


    @staticmethod
    def new() -> None:
        tc_reader: TcFileReader = TcFileReader()
        props: list = [
            'project-oficial-name',
            'entrypoints',
            'commands',
            'version',
            'target',
            'dotenv',
            'ignore',
            'langs',
        ]

        if ( err := tc_reader.add_filters(props=props) ).is_err():
            raise err.error

        tc_reader.build()
        if ( err := tc_reader.check_error() ).is_err():
            raise err.error

        project_content: ProjectSaver = ProjectSaver(metadata=tc_reader.value)
        if ( err := project_content.check_error() ).is_err():
            raise err.error

        print(project_content.value)


