try:
    from forge.mod import data
    from core.mod import data
    print('try')

except:
    from .forge.mod import data
    from .core.mod import data
    print('except')



forest: dict = {
    'core': data,
    '': data,
}

