#~>
from src.c_terminal.prelude import Terminal
from src.tcfmt.creator import TcFileCreator
from src.tcfmt.reader import TcFileReader
from src.core.result import Result


#.?
from .save_snippet import SnippetSaver
from .constants import TcSnippetConfig
from .errs import SnippetError
from .use import UseSnippet


#<·
class SnippetManager: # Ok
    @staticmethod # Ok
    def start() -> None:
        terminal_content: Terminal = Terminal(field=TcSnippetConfig.TEMPLATE_NAME)

        if ( err := terminal_content.check_error() ).is_err():
            raise err.error

        temp_name: str = terminal_content.value

        action: TcFileCreator = TcFileCreator(
            tempname=temp_name,
            root='snippet',
        )

        if ( err := action.check_error() ).is_err():
            raise err.error


    @staticmethod
    def new() -> None: # Ok
        action: TcFileReader = TcFileReader()
        if ( err :=action.add_filters(
            props=[
                'version',
                'target',
                'name',
                'type',
                'lang',
            ]
        ) ).is_err():
            raise err.error

        action.build()

        if ( err := action.check_error() ).is_err():
            raise err.error

        saved: SnippetSaver= SnippetSaver(
            metadata=action.final_content,
        )
        if ( err := saved.check_error() ).is_err():
            raise err.error

        print(f'new record with id: {saved.value}')


    @staticmethod # Ok
    def use(identifier: str) -> None:
        if not identifier:
            raise SnippetError(
                message='Invalid identifier',
                call='SnippetManager.use',
                source=__name__,
            )

        terminal_content: Terminal = Terminal(field=TcSnippetConfig.TEMPLATE_NAME)

        if ( err := terminal_content.check_error() ).is_err():
            raise err.error

        if ( err := UseSnippet(
            alias=terminal_content.value,
            identifier=identifier,
        ).check_error() ).is_err():
            raise err.error

