__author__ = 'rezenter'
import sys


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


def it_seq(*iterables):
    count = counter(iterables)
    it = iter(iterables)
    for i in range(0, count):
        tmp = next(it)
        tmp_count = counter(tmp)
        tmp_it = iter(tmp)
        for a in range(0, tmp_count):
            yield next(tmp_it)


def myrange(start=0, end=0, step=1):
    tmp = start
    if start > end:
        while tmp > end:
            yield tmp
            tmp += step
    elif start < end:
        while tmp < end:
            yield tmp
            tmp += step
    else:
        yield start


def it_merge(*iterables):
    count = counter(iterables)
    nums = []
    it = iter(iterables)
    i = 0
    while i < count:
        nums.append(counter(next(it)))
        i += 1
    a = sum(nums)
    starts = []
    tmp = 0
    while tmp < count:
        starts.append(0)
        tmp += 1
    while a > 0:
        its = []
        i = 0
        it = iter(iterables)
        elems = []
        tmp = 0
        while tmp < count:
            elems.append(sys.maxsize)
            tmp += 1
        while i < count:
            its.append(iter(next(it)))
            try:
                s = 0
                while s <= starts[i]:
                    elems[i] = next(its[i])
                    s += 1
            except StopIteration:
                if s == nums[i]:
                    elems[i] = sys.maxsize
            i += 1
        tmp = min(elems)
        yield tmp
        c = 0
        while c < count:
            if tmp == elems[c]:
                starts[c] += 1
                break
            c += 1
        a -= 1