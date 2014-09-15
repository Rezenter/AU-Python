__author__ = 'rezenter'

s4 = 'read'
snb = 'bhjkla adsf not adfl; bad ghk'
a = 'qwer'
b = 'aaabb'

def verbing(s):
    if len(s) > 2:
        n = s.find('ing')
        if n == -1:
            s += 'ing'
        else:
            s += 'ly'
    return s
print verbing(s4)

def not_bad(s):
    beg = s.find('not')
    end = s.find('bad')
    if beg != -1 and end != -1 and end > beg:
        res = s[0: beg]
        res += 'good'
        res += s[end+3:]
    else:
        res = s
    return res
print not_bad(snb)

def front_back(a, b):
    div1 = ((len(a))//2)+len(a) % 2
    div2 = ((len(b))//2)+len(b) % 2
    res = a[:div1]
    res += b[:div2]
    res += a[div1:]
    res += b[div2:]
    return res
print front_back(a, b)