from .core import FileManager, to_pkg
from .forge import data
from .mod import Tree


forest: dict = {
    'forge': Tree(data).build,
    'core': Tree(
        wood={
            'file': FileManager(),
            'pkg': to_pkg,
        }
    ).build
}
