#~>
from .fblank import Blank


factories: set = {
    Blank(),
}


data: dict = {f.tag: f for f in factories}
