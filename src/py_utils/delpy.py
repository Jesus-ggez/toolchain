import os


#~>


#<·
def search() -> None:
    raw: list = os.listdir()

    for dir_ in raw:
        if 'pycache' in dir_ and os.path.isdir(dir_):
            os.system(f'rm -r {dir_}')

    new: list = os.listdir()

    for dir_ in new:
        if os.path.isdir(dir_):
            try:
                os.chdir(dir_)
                search()

            except Exception as e:
                print(e)

            finally:
                os.chdir('..')

if __name__ == '__main__':
    search()
