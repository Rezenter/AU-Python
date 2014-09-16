__author__ = 'rezenter'

l = [1, 2, 2, 2, 3]
l1 = [1, 1, 2, 8]
l2 = [1, 3, 3, 4]


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
    if len(lst1) == 0:
        return lst2
    if len(lst2) == 0:
        return lst1
    global i2
    i2 = 0
    global i1
    i1 = 0
    while True:
        if i1 < len(lst1) and i2 < len(lst2):
            if lst1[i1] < lst2[i2]:
                lst.append(lst1[i1])
                i1 += 1
            else:
                lst.append(lst2[i2])
                i2 += 1
        else:
            if i1 < len(lst1):
                for i1 in range(i1, len(lst1)):
                    lst.append(lst1[i1])
                return lst
            else:
                for i2 in range(i2, len(lst2)):
                    lst.append(lst2[i2])
                return lst

print(linear_merge(l1, l2))
