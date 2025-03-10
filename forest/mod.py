try:
    from forge.mod import data as forge_data
    from core.mod import data as core_data
    print('try')

except ImportError:
    from .forge.mod import data as forge_data
    from .core.mod import data as core_data
    print('except')


forest: dict = {
    'core': core_data,
    'forge': forge_data,
}

