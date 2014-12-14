__author__ = 'rezenter'
import sys
import re
path = sys.argv[1]
file = open(path, 'r')
cl = re.compile("((?P<space>(( )+)|\t)*(?P<cod>class|def) (?P<name>[a-zA-Z_]+))")
count = 0
current = ""


def prev_cod(st):
    dot_find = re.compile("\.(?P<prev>[a-zA-Z_]+)$")
    prev = dot_find.match(st)
    if prev is not None:
        return len(prev.group("prev"))
    elif len(st) != 0:
        return len(st)
    return 0
for i in file:
    match = cl.match(i)
    if match is not None:
        if match.group("space") is not None:
            new_count = len(match.group("space"))
        else:
            new_count = 0
        if count == new_count:
            pass
        elif count > new_count:
            count = new_count
            current = current[0:len(current) - prev_cod(current)]
        else:
            if count == 0:
                count = new_count
        if match.group("cod") == "class":
            current += match.group("name")
        else:
            if len(current) != 0:
                print(current + "." + match.group("name"))
            else:
                print(match.group("name"))