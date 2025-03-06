import os


def replace(old: str, new: str) -> None:
    current: list = os.listdir()

    for file in current:
        if not os.path.isfile(file):
            continue

        file_replace(
            filename=file,
            old=old,
            new=new,
        )


def file_replace(filename: str, old: str, new: str) -> None:
    new_doc: list = []
    with open(filename, 'r') as old_file:
        for line in old_file:
            line.replace(old, new)

    with open(filename, 'w') as new_file:
        new_file.writelines(new_doc)
