#~>


#.?
from .pure_list import filt_list
from .pure_str import filt_str


#<·
data: dict = {
    '[': filt_list,
    '"': filt_str,
}
