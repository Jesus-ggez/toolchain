try:
    from x import main

except:
    from .x import main

data: dict = {
    'main': main
}
