__author__ = 'a'
file = open('nails.in', 'r')
n = int(file.readline())
s = file.readline().split()
file.close()
nails = []
for a in range(0, n):
    nails.append(int(s[a]))
result = 0
nails.sort()
if len(nails) >= 3:
    result = [0, nails[1] - nails[0], nails[2] - nails[0]]
    for i in range(3, len(nails)):
        result.append(min(result[i-1], result[i-2]) + nails[i] - nails[i-1])
        print(nails[i] - nails[i-1])
elif len(nails) == 2:
    result = [nails[1] - nails[0]]
else:
    result = [0]

print(result)
file = open('nails.out', 'w')
file.write(str(result[len(result) - 1]))
file.close()