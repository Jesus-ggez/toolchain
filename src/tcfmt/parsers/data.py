#~>


#.?
from .to_string import parse_to_string
from .to_list import parse_to_list


#<·
parsers: dict = {
    '"': parse_to_string,
    '[': parse_to_list,
}
