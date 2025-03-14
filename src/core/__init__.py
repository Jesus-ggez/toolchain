from .file_actions import (
    WriteManager,
    ReadManager,
    FileManager
)
from .to_pkg import to_pkg


data: dict = {
    'file': FileManager(),
    'pkg': to_pkg
}
