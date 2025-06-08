#~>


#<·
def tokenize(raw: str) -> list:
    valid_no_alnum: tuple = (
        '_',
    )
    data: list[str] = []

    word: str = ''

    for character in raw:
        if character.isalnum() or character in valid_no_alnum:
            word += character
            continue

        if not character.strip():
            continue

        if word:
            data.append(word)
            word = ''

        data.append(character)

    if word:
        data.append(word)

    return data


if __name__ == '__main__':
    with open('struct.tc', 'r') as data:
        string = data.read()

        res = tokenize(string)

        print(res)

