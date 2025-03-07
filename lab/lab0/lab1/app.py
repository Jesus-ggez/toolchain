try:
    from lab2.app import data as _data

except:
    from .lab2.app import data as _data


data: dict = {
    'lab2': _data,
}
