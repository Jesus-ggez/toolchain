#~>
from src.c_terminal.prelude import Terminal
from src.tcfmt.creator import TcFileCreator
from src.tcfmt.reader import TcFileReader


#.?
from .constants import TcProjectConfig
#from .save_project import SaveProject


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
        action: TcFileReader = TcFileReader()
        if ( err := action.add_filters(
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
        ) ).is_err():
            raise err.error

        action.build()

        if ( err := action.check_error() ).is_err():
            raise err.error

        print(action.final_content)
        """
        save_action: SaveProject = SaveProject(m=action.final_content)
        if ( err := save_action.check_error() ).is_err():
            raise err.error

        print(save_action)

        """


    @staticmethod
    def use() -> None:
        ...
