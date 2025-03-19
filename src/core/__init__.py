#~>
from .file_actions import (
    WriteManager,
    ReadManager,
    FileManager
)
from .del_pycache import delpy
from .to_pkg import to_pkg


data: dict = {
    'pkg': to_pkg,
    'delpy': delpy
}
