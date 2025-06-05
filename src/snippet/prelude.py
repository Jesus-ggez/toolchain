#~>
from src.c_terminal.prelude import Terminal
from src.tcfmt.creator import TcFileCreator
from src.tcfmt.reader import TcFileReader


#.?
from .save_snippet import SnippetSaver
from .constants import TcSnippetConfig
from .list_content import ListContent
from .errs import SnippetError
from .use import UseSnippet


#<·
class SnippetManager: # Ok
    @staticmethod # Ok
    def start() -> None:
        terminal_content: Terminal = Terminal(field=TcSnippetConfig.TEMPLATE_NAME)
        terminal_content.check_error().or_fail()

        TcFileCreator(
            tempname=terminal_content.value,
            root='snippet',
        ).or_fail()


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
        ).or_fail()

        action.build()
        action.or_fail()


        saved: SnippetSaver= SnippetSaver(metadata=action.value)
        saved.or_fail()

        print(f'new record with id: {saved.value}')


    @staticmethod # Ok
    def use(identifier: str) -> None:
        if not identifier:
            raise SnippetError(
                message='Invalid identifier',
                call='SnippetManager.use',
                source=__name__,
            )

        terminal_content: Terminal = Terminal(field=TcSnippetConfig.ALIAS)
        terminal_content.or_fail()

        action: UseSnippet = UseSnippet(
            alias=terminal_content.value,
            identifier=identifier,
        )

        action.or_fail()


    @staticmethod
    def list_all() -> None:
        action: ListContent = ListContent()

        action.or_fail()

        print(action.value)
