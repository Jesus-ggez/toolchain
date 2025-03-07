try:
    from lab0.app import data as _data

except:
    from .lab0.app import data as _data


data: dict = {
    'lab0': _data
}
