class ProjectDb:
    @staticmethod
    def add_in(
        composition: str,
        entrypoints: str,
        commands: str,
        version: str,
        langs: str,
        name: str,
        env: str,
    ) -> int: ...

    @staticmethod
    def get_by_id(id: int) -> str: ...

    @staticmethod
    def get_by_name(name_: str) -> str: ...

    @staticmethod
    def delete_project(id_: int) -> bool: ...


class SnippetDb:
    @staticmethod
    def set_snippet(name: str, content: str) -> int: ...

    @staticmethod
    def get_snippet(id: int) -> str: ...

    @staticmethod
    def delete_snippet(id_: int) -> bool: ...
