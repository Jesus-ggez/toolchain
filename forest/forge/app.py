try:
    from snippet.disable import disable_snippet
    from snippet.create import create_snippet
    from snippet.get_one import get_snippet
    from snippet.get_all import get_all

except:
    from .snippet.disable import disable_snippet
    from .snippet.create import create_snippet
    from .snippet.get_one import get_snippet
    from .snippet.get_all import get_all


class ForgeTree:
    def __init__(self, core_util: dict) -> None:
        self.file_manager: type = core_util['file']['pure_impl']

    def add_snippet(self, name: str) -> None:
        create_snippet(
            writer=self.file_manager.write,
            reader=self.file_manager.read,
            name=name,
        )

    def disable_snippet(self, id: str) -> None:
        disable_snippet(
            id=id,
        )


    def get_snippet(self, identifier: str) -> None:
        get_snippet(
            identifier=identifier,
        )


    def get_all(self) -> list:
        return get_all()




