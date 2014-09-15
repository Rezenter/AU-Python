__author__ = 'rezenter'

l = [1, 2, 2, 2, 3]
l1 = [1, 2, 8, 9, 10]
l2 = [3, 3, 3, 4]


def remove_adjacent(lst):
    res = []
    prev = None
    for i in range(0, len(lst)):
        tmp = lst.pop()
        if tmp != prev:
            res.append(tmp)
            prev = tmp
    res.reverse()
    return res
print remove_adjacent(l)

def linear_merge(lst1, lst2):
    lst = []
    if len(lst1) == 0:
        return lst2
    if len(lst2) == 0:
        return lst1
    t1 = lst1.pop(0)
    t2 = lst2.pop(0)
    while len(lst1) != 0:
        if t1 < t2:
            lst.append(t1)
            t1 = lst1.pop(0)

        else:
            lst.append(t2)
            if len(lst2) != 0:
                t2 = lst2.pop(0)
            else:
                lst.append(t1)
                lst.append(lst1)
                return lst

    while len(lst2) != 0:
        if t1 < t2:
            lst.append(t1)
            t1 = None
        else:
            lst.append(t2)
            if len(lst2) != 0:
                t2 = lst2.pop(0)
    lst.append(t2)
    if t1 is not None:
        lst.append(t1)
    return lst
print linear_merge(l1, l2)
