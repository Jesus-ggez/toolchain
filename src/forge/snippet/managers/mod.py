#~>
from src.core import FileManager
from .data import managers
from utils.result import (
    Result,
    Err,
    Ok,
)



def get_manager(name: str) -> Result[list, Exception]:
    if not (name in managers):
        return Err(error=Exception(
            'Manager name not found'
        ))

    actor: FileManager = FileManager()
    data: Result = actor.read.as_list(
        name=name,
    )

    if data.is_err():
        return Err(error=data.error)

    return Ok(data=data.data)
