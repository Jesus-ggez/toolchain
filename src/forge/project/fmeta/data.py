#~>
from .fcommands import CommandsFactoryMeta
from .fdotenv import DotEnvFactoryMeta
from .fignore import IgnoreFactoryMeta
from .fentry import EntryFactoryMeta
from .f_type import _TypeFactoryMeta
from .fbegin import BeginFactoryMeta
from .flangs import LangsFactoryMeta
from .fname import NameFactoryMeta


data: dict = {
    '#<~>': [
        CommandsFactoryMeta(),
        DotEnvFactoryMeta(),
        IgnoreFactoryMeta(),
        EntryFactoryMeta(),
        _TypeFactoryMeta(),
        BeginFactoryMeta(),
        LangsFactoryMeta(),
        NameFactoryMeta(),
    ]
}
