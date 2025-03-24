#~>
from .call_with_args import CallWithArgsFactory
from .call_with_arg import CallWithArgFactory
from .move_node import MoveNodeFactory
from .only_call import OnlyCallFactory

_all_data: set = {
    CallWithArgsFactory,
    CallWithArgFactory,
    MoveNodeFactory,
    OnlyCallFactory,
}

all_data: dict = {
    data.tag: data
    for data in _all_data
}
