def tokenize(raw: str) -> list:
    data: list = []
    word: str = ''
    mark: str = ''

    for character in raw:
        if character.isalnum() or character == '_':
            word += character
            if mark:
                data.append(mark)
                mark = ''
            continue
        mark += character
        if word:
            data.append(word)
            word = ''

    if mark:
        data.append(mark)
    if word:
        data.append(word)

    return data


if __name__ == '__main__':
    test: list = tokenize('!example:root->value_1')
    print(test)  # ['!', 'example', ':', 'root', '->', 'value_1']
