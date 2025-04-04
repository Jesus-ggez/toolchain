#~>
from .fsimple import Simple


_data: set = {
    Simple(),
}


data: dict = {
    item.type: item for item in _data
}
