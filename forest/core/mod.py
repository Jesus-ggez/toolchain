try:
    from file_manager import FileManager
    from to_pkg import build_pkg

except:
    from .file_manager import FileManager
    from .to_pkg import build_pkg


file_manager: FileManager = FileManager()
data: dict = {
    'pkg': build_pkg,
    'file': {
        'pure_impl': file_manager,
        'read': {
            'list': file_manager.read.as_list,
            'str': file_manager.read.as_str,
        },
        'write': {
            'logfile': file_manager.write.append_or_create,
            'list': file_manager.write.write_list,
            'str': file_manager.write.write_str,
        },
    },
}
