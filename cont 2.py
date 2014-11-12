__author__ = 'a'
import re
file = open('patterns.in', 'r')
pat = file.readline()
pat = pat[:len(pat) - 1]
s = file.readline()
file.close()
i = 0
patt = ''
while i < len(pat):
    char = pat[i]
    if char == '?':
        patt += '.'
    elif char == '*':
        patt += '(.)*'
    else:
        patt += char
    i += 1
pattern = re.compile(patt)
if re.match(pattern, s) is None:
    result = 'NO'
else:
    result = 'YES'
i = 0
while i < len(s) - 1:
    if s[i] != '.' and not s[i].isalpha():
        result = 'NO'
    i += 1
file = open('patterns.out', 'w')
file.write(str(result))
file.close()