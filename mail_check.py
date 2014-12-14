__author__ = 'rezenter'
import re

ip = "(\d\d\.|(\d\.|((([0-1]\d{2})|(2([0-4]\d)|2(5[0-5])))\.))){3}(\d\d|(\d|(([0-1]\d{2})|(2([0-4]\d)|2(5[0-5])))))"
qu = "(\"[ (),;:<>@\[\]\|a-zA-Z0-9!#\$%&`*+\-/=?^_{}|~]*(\{2})*(\\\\\")*[ (),;:<>@\[\]\|a-zA-Z0-9!#\$%&`*+\-/=?^_{}|~]*\")"
az = "([a-zA-Z0-9!#\$%&`*+\-/=?^_{}|~])"
end = "@(((([a-z])*)+\.([a-z])+)|(" + ip + "))$"
ili = "(" + qu + "|" + az + ")"
r = re.compile("^" + ili + "+" + "(\." + "(" + ili + ")+" + ")*" + end)


file = open('file.in', 'r')
adr = {}
for i in file:
    test_object = i
    if r.match(test_object) is not None:
        if test_object in adr:
            adr[test_object] += 1
        else:
            adr[test_object] = 1
file.close()
res = []
for i in adr:
    res.append([i, adr[i]])


def sort_by(arg):
    return arg[1]
res.sort(key=sort_by, reverse=True)
for i in res:
    print(i[0], i[1])