#~>
from .call_with_args import CallWithArgsFactory
from .call_with_arg import CallWithArgFactory
from .move_node import MoveNodeFactory
from .only_call import OnlyCallFactory


all_data: dict = {
    '::': CallWithArgFactory,
    '·': CallWithArgsFactory,
    ':': MoveNodeFactory,
    '.': OnlyCallFactory,
}

