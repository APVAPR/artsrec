import transliterate


def get_slug(*args):
    tmp = cut_titles(*args)
    tmp2 = []
    for i in tmp:
        if transliterate.detect_language(i) is None:
            tmp2.append(i)
        else:
            tmp2.append(transliterate.translit(i, reversed=True))
    return '-'.join(tmp2)


def cut_titles(*args):
    tmp = []
    for i in args:
        n = i.lower().split()
        if len(n) > 1:
            for j in n:
                tmp.append(j)
        else:
            tmp.append(*n)
    return tmp


