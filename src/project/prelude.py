#~>
from src.tcfmt.prelude import TcFileCreator, TcFileReader
from src.c_terminal.prelude import Terminal
from src.core.result import Result

#.?
from .constants import TcProjectConfig
from .errs import ProjectError

#<·
class ProjectManager:
    @staticmethod
    def start() -> None: # Ok?
        raw_temp_name: Terminal = Terminal(field=TcProjectConfig.TEMPLATE_NAME)

        if ( err := raw_temp_name.check_error() ).is_err():
            raise err.error

        temp_name: Result = raw_temp_name.get_field()
        if temp_name.is_err():
            raise temp_name.error

        action: TcFileCreator = TcFileCreator(root='project')
        action.create_document(
            tempname=temp_name.value
        )

        if ( err := action.check_error() ).is_err():
            raise err.error
