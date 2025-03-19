def _is_invalid_file(filename: str, bad_begin: tuple) -> bool:
    for _bad_begin in bad_begin:
        if filename.startswith(_bad_begin):
            return True

    return False

