import os

def rcv(name: str, foo: int) -> int:
    try:
        os.chdir(name)
        foo = read_lines(foo)
        os.chdir('..')

    except Exception as e:
        print(e, name)

    return foo


def read_lines(foo: int) -> int:
    data = os.listdir()

    for line in data:
        if line.startswith(('.', '_')):
            if not line.endswith('.py'):
                continue

        if os.path.isdir(line):
            foo = rcv(line, foo)
            continue

        try:
            with open(line, 'r') as doc:
                foo += len(doc.readlines())

        except Exception as e:
            print(f"Error leyendo {line}: {e}", os.getcwd())

    return foo

foo = 0
foo = read_lines(foo)
print(foo)

