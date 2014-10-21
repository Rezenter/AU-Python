__author__ = 'a'
file = open('joseph.in', 'r')
s = file.readline().split()
file.close()
n = int(s[0])
p = int(s[1])
lst = []
for i in range(1, n+1):
    lst.append(i)
a = len(lst)
while a != 1:
    tmp = p % a
    if tmp == 0:
        lst.pop()
    else:
        lst.pop(tmp-1)
    a = len(lst)
file = open('joseph.out', 'w')
file.write(str(lst[0]))
file.close()