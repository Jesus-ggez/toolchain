try:
    from lab1.app import data as _data

except:
    from .lab1.app import data as _data


data: dict = {
    'lab1': _data
}
