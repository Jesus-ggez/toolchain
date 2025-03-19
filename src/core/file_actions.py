class WriteManager:
    def from_list(self, name: str, content: list) -> None:
        with open(name, 'w') as data:
            data.writelines(content)


    def from_str(self, name: str, content: str) -> None:
        with open(name, 'w') as data:
            data.write(content)


    def ensure_exists(self, name: str, content: str | list) -> None:
        with open(name, 'a') as data:
            if isinstance(content, str):
                data.write(content + '\n')
                return

            data.writelines(content)


class ReadManager:
    def as_str(self, name: str) -> str:
        with open(name, 'r') as data:
            return data.read()


    def as_list(self, name: str) -> list:
        with open(name, 'r') as data:
            return data.readlines()


class FileManager:
    def __init__(self) -> None:
        self.write: WriteManager = WriteManager()
        self.read: ReadManager = ReadManager()
