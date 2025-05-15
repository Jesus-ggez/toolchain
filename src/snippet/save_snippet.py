from typing import Any
import os


#¿?
from snippet_db import SnippetDb


#~>
from src.tcfmt.constants import TcConfig
from src.core.file_utils import Reader
from src.core.errors import safe_exec
from src.core.result import (
    Result,
    Err,
    Ok,
)


#.?
from .errs import MetadataError


#<·

def save_snippet(metadata: dict) -> Result[int, MetadataError]:
    if not ('target' in metadata):
        return Err(error=MetadataError(
            message='Invalid target for reading',
            call='save_snippet()',
            source=__name__,
        ))

    data: Result = Reader.as_str(
        filename=metadata['target'],
    )
    if data.is_err():
        return data

    if not ('name' in metadata):
        return Err(error=MetadataError(
            message='Invalid format to snippet name',
            call='save_snippet()',
            source=__name__,
        ))

    dot: str = '.'
    res: Result = ward(
        name=metadata['name'] + dot + metadata.get('lang', 'txt'),
        version=metadata.get('version', '0.0.0'),
        _type=metadata.get('type', 'test'),
        content=data.value,
    )

    if res.is_err():
        return Err(error=res.error)

    if ( err := remove_document() ).is_err():
        return err

    return Ok(res.value)


@safe_exec # raise rust.diesel.error or int::i32
def ward(name: str, version: str, _type: str, content: str) -> Any:
    return SnippetDb.add_in(
        version=version,
        content=content,
        _type=_type,
        name=name,
    )

@safe_exec # raise Exception or None
def remove_document() -> Any:
    os.remove(TcConfig.FILE_NAME)
