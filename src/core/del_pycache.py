import shutil, os

#~>
from utils.result import (
    Result,
    Err,
    Ok,
)


def recursive_call(dirname: str) -> Result[None, Exception]:
    try:
        os.chdir(dirname)
        delpy()

    except Exception as e:
        print(e)
        return Err(error=e)

    return Ok()


def delpy() -> None:
    raw: list[str] = os.listdir()

    for dirname in raw:
        if 'pycache' in dirname and os.path.isdir(dirname):
            shutil.rmtree(dirname)
            break

    new: list[str] = os.listdir()

    for dirname in new:
        if not os.path.isdir(dirname):
            continue

        _action: Result = recursive_call(
            dirname=dirname,
        )
        if _action.is_err():
            print(_action)
        os.chdir('..')


if __name__ == '__main__':
    delpy()
