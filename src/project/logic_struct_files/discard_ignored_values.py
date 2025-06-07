#~>
from src.identity.dir_object import DirVO


#<·
def discard_values(item_refr: DirVO, ignored: list) -> None:
    if not ignored:
        return

    files: list[str] = item_refr.files.copy()
    dirs: list[str] = item_refr.dirs.copy()
    star: str = '*'

    for item in ignored:
        if item.endswith(star):
            ignore_prfx: str = item.removesuffix(star)

            item_refr.files.clear()
            item_refr.files.extend(
                file for file in files
                if not file.startswith(ignore_prfx)
            )

            item_refr.dirs.clear()
            item_refr.dirs.extend(
                dir_ for dir_ in dirs
                if not dir_.startswith(ignore_prfx)
            )

            continue

        if item.endswith(star):
            ignore_sfx: str  = item.removeprefix(star)

            item_refr.files.clear()
            item_refr.files.extend(
                file for file in files
                if not file.endswith(ignore_sfx)
            )

            item_refr.dirs.clear()
            item_refr.dirs.extend(
                dir_ for dir_ in dirs
                if not dir_.endswith(ignore_sfx)
            )

            continue

        if item in files:
            item_refr.files.remove(item)

        if item in dirs:
            item_refr.dirs.remove(item)
