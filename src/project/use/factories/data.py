#.?
from .create_files_from_stack import CreateFilesFromStack
from .increment_file_stack import IncrementFileStack
from .start_context import StartContext
from .end_context import EndContext
from .create_dir import CreateDir


#<·
data: dict = {
    ';': CreateFilesFromStack,
    ',': IncrementFileStack,
    '{': StartContext,
    '}': EndContext,
    '.': CreateDir,
}
