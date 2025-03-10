import os

#~>
from file_manager import FileManager
from checks import __is_invalid_file
from langs import langs, Lang


def __re_call(
    depth: int | None,
    current: str,
    dirname: str,
    lang: str,
) -> None:
    try:
        os.chdir(dirname)
        build_pkg(
        depth=depth - 1 if isinstance(depth, int) else None,
        lang=lang,
    )

    except Exception as e:
        print(e)

    finally:
        if os.getcwd() != current:
            os.chdir(current)


#   ···   only python use   ···   #
def build_pkg(
    lang: str,
    depth: int | None = None,
) -> None:
    if not (depth is None) and depth <= 0: return

    config: Lang | None = langs.get(lang)
    if config is None:
        raise ValueError('Unknown lang')

    file_context: FileManager = FileManager()
    current: str = os.getcwd()
    pkg_values: dict = {}

    for item in os.listdir():
        if __is_invalid_file(
            invalid_values=config.invalid_start,
            extension=config.extension,
            filename=item,
        ): continue

        if os.path.isdir(item):
            __re_call(
                current=current,
                dirname=item,
                depth=depth,
                lang=lang,
            ); continue

        file_content: list[str] = file_context.read.as_list(name=item)
        filename: str = item.split('.')[0]

        file_export_values: list[str] = [
            # separe funcs and cls
            line.split()[1]
            for line in file_content
            if line.startswith(config.export)
        ]
        file_export_values = [
            next(
                (
                    line.split(c_end)[0]
                    for c_end in config.conflictive
                    if c_end in line
                ), line
            ) for line in file_export_values
            if not line.startswith('_')
        ]

        if file_export_values:
            pkg_values[filename] = file_export_values

    if not pkg_values: return
    pkg_name: str = config.pkg_name

    for filename, exports in pkg_values.items():
        if len(exports) == 1:
            file_context.write.append_or_create(
                name=pkg_name,
                content=[config.import_(filename, exports.pop())]
            ); continue

        tab: str = '    '
        exports: list = [tab + v for v in exports]

        file_context.write.append_or_create(
            name=pkg_name,
            content=[
                config.import_(filename, '('),
                ',\n'.join(exports),
                '\n)\n',
            ]
        )
