class FileReader:
    def as_str(self, name: str) -> str:
        with open(name, 'r') as file:
            return file.read()


    def as_list(self, name: str) -> list:
        with open(name, 'r') as file:
            return file.readlines()


class FileWriter:
    def write_str(self, name: str, content: str) -> None:
        with open(name, 'w') as doc:
            doc.write(content)


    def write_list(self, name: str, content: list) -> None:
        with open(name, 'w') as doc:
            doc.writelines(content)


    def append_or_create(self, name: str, content: list) -> None:
        try:
            with open(name, 'a') as doc:
                doc.writelines(content)

        except FileNotFoundError:
            self.write_list(name=name, content=content)


class FileManager:
    write: FileWriter = FileWriter()
    read: FileReader = FileReader()
