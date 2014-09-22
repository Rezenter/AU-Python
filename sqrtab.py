__author__ = 'rezenter'
import math
file_in = open('sqrtab.in', 'r')
all = file_in.readlines()
n = all[0]
file_in.close()

def find(num):
    mid = int(math.pow(num, 0.5))
    if num == 1:
        return 0
    count = 0
    for a in range(1, mid+1):
        tmp = math.pow(num - math.pow(a, 2), 0.5)
        if tmp == int(tmp):
            count += 1
    return count
file_out = open('sqrtab.out', 'w')
for i in range(1, int(n) + 1):
    file_out.write(str(find(int(all[i]))))
    if i != int(n):
        file_out.write('\n')
file_out.close()