#~>
from .fversion import VersionFactory
from .ftarget import TargetFactory
from .fname import NameFactory
from .flang import LangFactory
from .ftype import TypeFactory

basic: tuple = (
    VersionFactory,
    TargetFactory,
    NameFactory,
    LangFactory,
    TypeFactory,
)

data: dict = {
    '#·!': basic,
}
