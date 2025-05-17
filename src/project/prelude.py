#~>
from src.c_terminal.prelude import Terminal
from src.tcfmt.creator import TcFileCreator
from src.core.result import Result


#.?
from .constants import TcProjectConfig


#<·
class ProjectManager:
    @staticmethod
    def start() -> None: # Ok?
        terminal_content: Terminal = Terminal(field=TcProjectConfig.TEMPLATE_NAME)
        if ( err := terminal_content.check_error() ).is_err():
            raise err.error

        action: TcFileCreator = TcFileCreator(
            tempname=terminal_content.value,
            root='project',
        )

        if ( err := action.check_error() ).is_err():
            raise err.error
