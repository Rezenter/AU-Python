__author__ = 'rezenter'

s4 = 'read'
snb = 'bhjkla adsf not adfl; bad ghk'

def verbing(s):
    if len(s) > 2:
        n = s.find('ing')
        if n == -1:
            s += 'ing'
    return s
print(verbing(s4))

def not_bad(s):
    beg = s.find(' not ')
    end = s.find(' bad ')
    if beg != -1 and end != -1 and end > beg:
        res = s[0: beg]
        res += ' good'
        res += s[end:]
    return res
print(not_bad(snb))

