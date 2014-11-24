__author__ = 'rezenter'


def myfilter(func, iterable):
    for i in iterable:
        if func(i):
            yield i


def myreduce(func, iterable, initializer=0):
    acc = initializer
    for i in iterable:
        acc = func(acc, i)
    return acc


def counter(iterable):
    count = 0
    it = iter(iterable)
    while True:
        try:
            next(it)
            count += 1
        except StopIteration:
            break
    return count


def mymap(func, *iterable):
    count = counter(iterable)
    it = iter(iterable)
    mi = counter(next(it))
    i = 1
    while i < count:
        tmp = counter(next(it))
        if tmp < mi:
            mi = tmp
        i += 1
    ar = []
    a = 0
    while a < mi:
        c = 0
        it = iter(iterable)
        while c < count:
            tmpit = iter(next(it))
            i = 0
            while i < a:
                next(tmpit)
                i += 1
            ar.append(next(tmpit))
            c += 1
        yield func(*ar)
        ar = []
        a += 1


def lister(iterable):
    result = []
    it = iter(iterable)
    for i in range(0, counter(iterable)):
        result.append(next(it))
    return result


def myzip(*iterable):
    it = iter(iterable)
    iterables = []
    for i in range(0, counter(iterable)):
        iterables.append(lister(next(it)))
    mi = counter(iterables[0])
    i = 0
    while i < len(iterables):
        if counter(iterables[i]) < mi:
            mi = counter(iterables[i])
        i += 1
    i = 0
    result = []
    while i < mi:
        result.append([])
        a = 0
        while a < len(iterables):
            it = iter(iterables[a])
            for v in range(0, i + 1):
                tmp = next(it)
            result[i].append(tmp)
            a += 1
        result[i] = tuple(result[i])
        yield result[i]
        i += 1


def foreach(func, iterable):
    for i in iterable:
        func(i)


def composition(f1, f2):
    return lambda x: f1(f2(x))


def bind1st(func, x):
        return lambda y: func(x, y)


def bind2nd(func, y):
        return lambda x: func(x, y)
