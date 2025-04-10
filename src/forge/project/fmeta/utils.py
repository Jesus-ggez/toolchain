def fmt_to_list(v: str) -> str:
    begin, end = '[]'
    if begin in v:
        v = v.replace(begin, '')

    if end in v:
        v = v.replace(end, '')

    return v
