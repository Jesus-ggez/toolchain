def __is_invalid_file(filename: str, invalid_values, extension: str) -> bool:
    if not filename.endswith(extension):
        return True

    for invalid_prefix in invalid_values:
        if filename.startswith(invalid_prefix):
            return True

    return False
