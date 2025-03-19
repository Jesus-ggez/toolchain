import sys
import os

#~>
try: # package file
    from .file_actions import FileManager
    from .filters import _is_invalid_file
    from .langs import langs, Lang

except ImportError: # local file
    from file_actions import FileManager
    from filters import _is_invalid_file
    from langs import langs, Lang


def __mv_node(filename: str, lang: str, depth: int | None, current: str) -> None:
    try:
        os.chdir(filename)
        to_pkg(depth=depth, lang=lang)
        os.chdir('..')

    except Exception as e: print(e)

    finally:
        if os.getcwd() != current:
            os.chdir(current)

def __only_dir(config) -> None:
    if not sys.argv:
        return

    n: int = 0
    if sys.argv[0] == __name__:
        n += 1

    pura_cmd: list[str] = sys.argv[n:]
    print(len(pura_cmd))

    if len(pura_cmd) == 1:
        print(f'solo en: {pura_cmd[0]}')
        if os.path.isdir(pura_cmd[0]):
            os.chdir(pura_cmd[0])
            return

    if len(pura_cmd) == 2:
        print('con flag')
        flag, dirname = pura_cmd

        print(os.getcwd())
        print('::48')
        if not os.path.isdir(dirname):
            print('no es file: ' + dirname)
            return

        os.chdir(dirname)
        print(os.getcwd())
        print('pre call flags :: 53')
        flags: dict = {
            'reset': lambda : os.remove(config.pkg_name)
        }

        if flag.startswith('--'):
            try:
                flags[flag.removeprefix('--')]()
                print('reset')
            except Exception as e:
                print(e)
        return


def to_pkg(lang: str, depth: int | None = None) -> None:
    if isinstance(depth, int):
        if depth <= 0: return
        depth -= 1

    config: Lang | None = langs.get(lang)
    if config is None:
        raise ValueError('Language are invalid')

    __only_dir(config)
    current: str = os.getcwd()
    pkg_values: dict[str, list] = {}

    for file in os.listdir():
        if _is_invalid_file(
            bad_begin=config.ignore_file,
            filename=file,
        ): continue

        print('ok')
        if os.path.isdir(file):
            __mv_node(
                current=current,
                filename=file,
                depth=depth,
                lang=lang,
            )
            continue

        if not file.endswith(config.extension):
            continue

        # document reader
        original_content: list[str] = FileManager().read.as_list(name=file)
        export_content: list[str] = []

        force_ignore: str = '#<·'
        force_add: str = '#·>' #<·
        for line in original_content:
            if force_ignore in line:
                continue

            if force_add in line:
                export_name: str = line.split(':')[0]
                export_content.append(export_name)
                continue


            if line.startswith(config.export):
                _parts: list = line.split()

                if len(_parts) <= 1:
                    continue

                _export_name: str = _parts[1]

                if _export_name.startswith(config.unexport):
                    continue

                export_name: str = next(
                    (
                        _export_name.split(end)[0]
                        for end in config.conflict
                        if end in _export_name
                    ), _export_name
                )
                export_content.append(export_name)
                continue


        if export_content:
            _filename: str = file.split('.')[0]
            pkg_values[_filename] = export_content


    if not pkg_values: return
    pkg_name: str = config.pkg_name

    for filename, exports in pkg_values.items():
        if len(exports) == 1:
            FileManager().write.ensure_exists(
                content=config.import_line(filename) + exports.pop(),
                name=pkg_name,
            )
            continue

        tab: str = '    '
        exports: list = [tab + v for v in exports]

        _content: list = [
            config.import_line(filename) + '(\n',
            ',\n'.join(exports),
            '\n)\n'
        ]
        FileManager().write.ensure_exists(
            content=_content,
            name=pkg_name,
        )


if __name__ == '__main__':
    to_pkg('py')
