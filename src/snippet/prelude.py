#~>
from src.tcfmt.prelude import TcFileCreator, TcFileReader
from src.c_terminal.prelude import Terminal
from src.core.result import Result

#.?
from .save_snippet import save_snippet
from .constants import TcSnippetConfig
from .errs import SnippetError
from .use import UseSnippet

#<·
class SnippetManager: # Ok
    @staticmethod # Ok
    def start() -> None:
        raw_temp_name: Terminal = Terminal(field=TcSnippetConfig.TEMPLATE_NAME)

        if ( err := raw_temp_name.check_error() ).is_err():
            raise err.error

        temp_name: Result = raw_temp_name.get_field()
        if temp_name.is_err():
            raise temp_name.error

        action: TcFileCreator = TcFileCreator(root='snippet')
        action.create_document(
            tempname=temp_name.value,
        )

        if ( err := action.check_error() ).is_err():
            raise err.error


    @staticmethod
    def new() -> None: # Ok
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

        saved: Result = save_snippet(metadata=action.final_content)
        if saved.is_err():
            raise saved.error

        print(f'new record with id: {saved.value}')


    @staticmethod # Ok
    def use(identifier: str) -> None:
        if not identifier:
            raise SnippetError(
                message='Invalid identifier',
                call='SnippetManager.use',
                source=__name__,
            )

        alias: Terminal = Terminal(field=TcSnippetConfig.ALIAS)
        if ( err := alias.check_error() ).is_err():
            raise err.error

        alias_v: Result = alias.get_field()
        if alias_v.is_err():
            raise alias_v.error

        action: UseSnippet = UseSnippet(
            identifier=identifier,
            alias=alias_v.value,
        )

        if ( err := action.check_error() ).is_err():
            raise err.error
