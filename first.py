__author__ = 'rezenter'

l = [1, 2, 2, 2, 3]
l1 = [1, 3, 5, 7, 8]
l2 = [2, 4, 6]


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
print(remove_adjacent(l))

def linear_merge(lst1, lst2):
    lst = []
    i = 0
    while len(lst1) != 0 and len(lst2) != 0:
        t1 = lst1.pop(i)
        t2 = lst2.pop(i)
        if t1 < t2:
            lst.append(t1)
            lst.append(t2)
        else:
            lst.append(t2)
            lst.append(t1)
        i+1
    if len(lst1) != 0:
        lst.extend(lst1)
    else:
        lst.extend(lst2)
    return lst
print(linear_merge(l1, l2))
