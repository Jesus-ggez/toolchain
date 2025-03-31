#~>
from .fversion import VersionFactory
from .fname import NameFactory
from .flang import LangFactory
from .ftype import TypeFactory


data: dict = {
    '#·!': [
        VersionFactory,
        NameFactory,
        LangFactory,
        TypeFactory,
    ],
}
