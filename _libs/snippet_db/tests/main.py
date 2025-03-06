from snippet_db import SnippetDb, ProjectDb


def snippet() -> None:
    raw: str = ''
    with open('foo.py', 'r') as doc:
        raw = doc.read()

    try:
        SnippetDb.add_in(
            'foo',
            '0.0.1',
            raw,
            'test',
        )
    except:
        print('existe en SnippetDb')


def find_snippet() -> None:
    values = SnippetDb.find_all()
    print(f'active values: {len(values)}')

    print('discard id:1')
    SnippetDb.discard(1)

    values = SnippetDb.find_all()
    print(f'active values: {len(values)}')

    try:
        v = SnippetDb.find_by_id(1)
        print(f'snippet with id:1 values: {v.name}')
    except Exception as e:
        print(e)


def project() -> None:
    try:
        ProjectDb.add_in(
            'foo',
            '0.0.1',
            'dirname·001002003004<·dirname_d0·dirname_d1·dirname·001<·<·<·'
        )
    except:
        print('existe en ProjectDb')


def find_project() -> None:
    values = ProjectDb.find_all()
    print(f'active values ProjectDb: {len(values)}')

    print('discard id:1')
    ProjectDb.discard(1)

    values = ProjectDb.find_all()
    print(f'active values ProjectDb: {len(values)}')

    try:
        v = ProjectDb.find_by_id(1)
        print(f'snippet with id:1 values: {v.name}')
    except Exception as e:
        print(e)



if __name__ == '__main__':
    snippet()
    project()
    find_snippet()
    find_project()
