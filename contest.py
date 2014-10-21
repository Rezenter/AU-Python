__author__ = 'a'

file = open('queue.in', 'r')
n = int(file.readline())
t = 0
arr = {}
lst = []
result = ''
last = 0
flag = 0


def check(r):
    if len(lst) != 0:
        if arr.get(lst[0][0], -1) > 0:
            r += str(t-lst[0][1]) + ' '
            arr[lst.pop(0)[0]] -= 1
            global flag
            flag = 1
    return r

for i in range(0, n):
    string = file.readline().split(' ')
    t = int(string[1])
    if int(string[0]) == 1:
        arr[int(string[2])] = 1
    else:
        tmp = [int(string[2]), int(string[1])]
        lst.append(tmp)
    result = check(result)
    while flag == 1:
        flag = 0
        result = check(result)
file.close()
while len(lst) != 0:
    lst.pop(0)
    result += '-1 '
print(result)
file = open('queue.out', 'w')
file.write(result)
file.close()