__author__ = 'rezenter'
import re
file = open('text.in', 'r')
# as the task mentioned that only one string will be given
st = file.readline().split()
# as for me all symbols except letters are break-symbols
abc = "([A-Za-zА-Яа-я]+)"
reg = re.compile(abc)


def generator(string):
    for i in string:
        match = reg.match(i)
        yield match.group()
        if len(match.group()) != len(i):
            yield i[len(match.group()):]
nextgen = generator(st)
for i in nextgen:
    print(i)
print(list(generator(st)))
