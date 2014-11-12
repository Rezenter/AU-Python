__author__ = 'rezenter'


def myfilter(func, iterable):
    result = []
    for i in iterable:
        if func(i):
            result.append(i)
    return result


def myreduce(func, iterable, *args):
    if len(args) == 0:
        init = 0
    else:
        init = args[0]
    flag = True
    last = 0
    for i in iterable:
        if not flag:
            last = func(last, i)
        else:
            last = init
            flag = False
    return last


def mymap(func, *iterable):
    mi = len(iterable[0])
    i = 0
    while i < len(iterable):
        if len(iterable[i]) < mi:
            mi = len(iterable[i])
        i += 1
    result = []
    ar = []
    a = 0
    while a < mi:
        c = 0
        while c < len(iterable):
            ar.append(iterable[c][a])
            c += 1
        result.append(func(*ar))
        ar = []
        a += 1
    return result


def myzip(*iterable):
    mi = len(iterable[0])
    i = 0
    while i < len(iterable):
        if len(iterable[i]) < mi:
            mi = len(iterable[i])
        i += 1
    i = 0
    result = []
    while i < mi:
        result.append([])
        a = 0
        while a < len(iterable):
            result[i].append(iterable[a][i])
            a += 1
        result[i] = tuple(result[i])
        i += 1
    return result


def foreach(func, iterable):
    for i in iterable:
        func(i)


def composition(f1, f2):
    return lambda x: f1(f2(x))