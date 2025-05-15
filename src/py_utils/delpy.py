import os


#~>


#<·
def search() -> None:
    raw: list = os.listdir()

    for dir in raw:
        if 'pycache' in dir and os.path.isdir(dir):
            os.system(f'rm -r {dir}')

    new: list = os.listdir()

    for dir in new:
        if os.path.isdir(dir):
            try:
                os.chdir(dir)
                search()

            except Exception as e:
                print(e)

            finally:
                os.chdir('..')
    return

