#~>
import os
from utils.result import (
    Result,
    Err,
    Ok,
)


class WriteManager:
    def from_list(self, name: str, content: list) -> Result[None, Exception]:
        try:
            with open(name, 'w') as data:
                data.writelines(content)

        except Exception as e:
            return Err(error=Exception(
                f"""from_list | The file could not be created
                {e}"""
            ))

        return Ok()


    def from_str(self, name: str, content: str) -> Result[None, Exception]:
        try:
            with open(name, 'w') as data:
                data.write(content)

        except Exception as e:
            return Err(error=Exception(
                f"""from_str | The file could not be created
                {e}"""
            ))

        return Ok()


    def extends(self, name: str, content: list) -> Result[None, Exception]:
        try:
            with open(name, 'a') as data:
                data.writelines(content)

        except Exception as e:
            return Err(error=Exception(
                f'extends | {e}'
            ))

        return Ok()


    def ensure_exists(self, name: str, content: str | list) -> Result[None, Exception]:
        if not content:
            return Err(error=Exception(
                """ensure_exists | Content cannot be empty"""
            ))

        if isinstance(content, str):
            content = [content]

        if not os.path.exists(name):
            return self.from_list(name=name, content=content)

        return self.extends(name=name, content=content)


class ReadManager:
    def as_str(self, name: str) -> Result[str, Exception]:
        try:
            with open(name, 'r') as data:
                final: str = data.read()

        except Exception as e:
            return Err(error=e)

        return Ok(final)


    def as_list(self, name: str) -> Result[list, Exception]:
        try:
            with open(name, 'r') as data:
                final: list[str] = data.readlines()

        except Exception as e:
            return Err(error=e)

        return Ok(final)


class FileManager:
    def __init__(self) -> None:
        self.write: WriteManager = WriteManager()
        self.read: ReadManager = ReadManager()
