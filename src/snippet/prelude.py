#~>
from src.tcfmt.prelude import TcFileCreator, TcFileReader
from src.c_terminal.prelude import Terminal
from src.core.result import Result

#.?

#<·
class SnippetManager:
    @staticmethod
    def start() -> None:
        temp_name: Terminal = Terminal(field='temp_name')

        if ( err := temp_name.check_error() ).is_err():
            raise err.error

        value: Result= temp_name.get_field()
        if value.is_err():
            raise value.error

        action: TcFileCreator = TcFileCreator()
        action.create_document(
            tempname=value.value or '_',
        )

        if ( err := action.check_error() ).is_err():
            raise err.error


    @staticmethod
    def new() -> None:
        action: TcFileReader = TcFileReader()
        action.add_filters(
            props=[
                'version',
                'target',
                'name',
                'type',
                'lang',
            ]
        )
        action.build()

        if ( err := action.check_error() ).is_err():
            raise err.error

        print(action.final_content)


