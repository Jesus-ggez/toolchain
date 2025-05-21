#~>


#<·
class TestGuideCases:
    zero_values: dict = {
        'str': ['', ' ', '\n', str()],
        'int': [0, int()],
        'float': [0.0, float()],
        'bool': [False, bool()],

        'tuple': [(), tuple()],
        'list': [[], list()],
        'dict': [{}, dict()],
        'set': [set()],
        'frozenset': [frozenset()],
    }
