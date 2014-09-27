__author__ = 'a'


'sorted(iterable[,key][,reverse])'
'lst = ["ccc", "fff"]' \
'sorted(lst)' \
'def third elem(s)' \
'   return s[2]' \
'sorted(lst, key = third_elem) will sort by third elem' \
'' \
'solid block of variables' \
'date_tuple = (day, month, year) but u can use lists instead of tuples' \
'print(date_tuple[:3])' \
'' \
'' \
'indexin on a key' \
''
wages = [('a a', 1), ('a b', 2), ('b b', 3)]


def get_wage(w_name):

    for (name, wage) in wages:
        if name == w_name:
            return wage
    return None
print(get_wage('b b'))
print(ord('а'))
print(ord('я'))
print(ord('А'))
print(ord('Я'))
''
