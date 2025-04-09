#~>
from .fcommands import CommandsFactory
from .fdotenv import DotEnvFactory
from .fignore import IgnoreFactory
from .fentry import EntryFactory
from .f_type import _TypeFactory
from .fbegin import BeginFactory
from .flangs import LangsFactory
from .fname import NameFactory


data: dict = {
    'blank': [
        CommandsFactory,
        DotEnvFactory,
        IgnoreFactory,
        EntryFactory,
        _TypeFactory,
        BeginFactory,
        LangsFactory,
        NameFactory,
    ]
}
