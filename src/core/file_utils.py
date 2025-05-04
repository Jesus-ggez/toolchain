#~>
from .errs import FileReaderError, FileWriterError
from .result import (
    Result,
    Err,
    Ok,
)


#<·
class Reader:
    @staticmethod
    def as_list(filename: str) -> Result[list, FileReaderError]:
        try:
            with open(filename, 'r') as file:
                return Ok(file.readlines())

        except Exception as e:
            return Err(error=FileReaderError(
                call='Reader.as_list',
                source=__name__,
                message=str(e),
            ))


    @staticmethod
    def as_str(filename: str) -> Result[str, FileReaderError]:
        try:
            with open(filename, 'r') as file:
                return Ok(file.read())

        except Exception as e:
            return Err(error=FileReaderError(
                call='Reader.as_str',
                source=__name__,
                message=str(e),
            ))


class Writer:
    @staticmethod
    def from_list(content: list, name: str) -> Result[None, FileWriterError]:
        try:
            with open(name, 'w') as file:
                file.writelines(content)
                return Ok()

        except Exception as e:
            return Err(error=FileWriterError(
                call='Writer.from_list',
                source=__name__,
                message=str(e),
            ))

    @staticmethod
    def from_str(content: str, name: str) -> Result[None, FileWriterError]:
        try:
            with open(name, 'w') as file:
                file.write(content)
                return Ok()

        except Exception as e:
            return Err(error=FileWriterError(
                call='Writer.from_str',
                source=__name__,
                message=str(e),
            ))


    @staticmethod
    def extends(content: list, name: str) -> Result[None, FileWriterError]:
        try:
            with open(name, 'a') as file:
                file.writelines(content)
                return Ok()

        except Exception as e:
            return Err(error=FileWriterError(
                call='Writer.extends',
                source=__name__,
                message=str(e),
            ))
