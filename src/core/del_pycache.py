import shutil, os

#~>

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

        try:
            os.chdir(dirname)
            delpy()

        except Exception as e:
            print(e)

        finally:
            os.chdir('..')
    return


if __name__ == '__main__':
    delpy()
