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
        terminal_content.ensure_ok()

        TcFileCreator(
            tempname=terminal_content.value,
            root='snippet',
        ).ensure_ok()


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
        ).ensure_ok()

        action.build()
        action.ensure_ok()


        saved: SnippetSaver= SnippetSaver(metadata=action.value)
        saved.ensure_ok()

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
        terminal_content.ensure_ok()

        action: UseSnippet = UseSnippet(
            alias=terminal_content.value,
            identifier=identifier,
        )

        action.ensure_ok()

        print('Project created succesfully')


    @staticmethod
    def list_all() -> None:
        action: ListContent = ListContent()

        action.ensure_ok()

        print(action.value)
