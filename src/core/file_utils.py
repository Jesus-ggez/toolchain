from typing import Any


#~>


#.?
from .errs import FileReaderError, FileWriterError
from .result import (
    Result,
    Err,
    Ok,
)


#<·
class Reader:
    @staticmethod
    def create_error(call_msg: str, e) -> Result[Any, FileReaderError]:
        return Err(error=FileReaderError(
            source=__name__,
            message=str(e),
            call=call_msg,
        ))


    @staticmethod
    def as_list(filename: str) -> Result[list, FileReaderError]:
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return Ok(file.readlines())

        except Exception as e:
            return Reader.create_error(call_msg='Reader.as_list', e=e)


    @staticmethod
    def as_str(filename: str) -> Result[str, FileReaderError]:
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return Ok(file.read())

        except Exception as e:
            return Reader.create_error(call_msg='Reader.as_str', e=e)


class Writer:
    @staticmethod
    def create_error(call_msg: str, e) -> Result[Any, FileWriterError]:
        return Err(error=FileWriterError(
            source=__name__,
            message=str(e),
            call=call_msg,
        ))


    @staticmethod
    def from_list(content: list, name: str) -> Result[None, FileWriterError]:
        try:
            with open(name, 'w', encoding='utf-8') as file:
                file.writelines(content)
                return Ok()

        except Exception as e:
            return Writer.create_error(call_msg='Writer.from_list', e=e)


    @staticmethod
    def from_str(content: str, name: str) -> Result[None, FileWriterError]:
        try:
            with open(name, 'w', encoding='utf-8') as file:
                file.write(content)
                return Ok()

        except Exception as e:
            return Writer.create_error(call_msg='Writer.from_str', e=e)


    @staticmethod
    def extends(content: list, name: str) -> Result[None, FileWriterError]:
        try:
            with open(name, 'a', encoding='utf-8') as file:
                file.writelines(content)
                return Ok()

        except Exception as e:
            return Writer.create_error(call_msg='Writer.extends', e=e)
