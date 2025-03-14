from .core import FileManager, to_pkg
from .forge import data

forest: dict = {
    'forge': data,
    'core': {
        'file': FileManager(),
        'pkg': to_pkg,
    }
}
