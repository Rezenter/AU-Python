__author__ = 'a'
file = open('nails.in', 'r')
n = int(file.readline())
s = file.readline().split()
file.close()
nails = []
for a in range(0, n):
    nails.append(int(s[a]))
result = 0
nails.sort(reverse=True)
i = 0
if n % 2 == 0:
    while i in range(0, n-1):
        result += nails[i] - nails[i + 1]
        i += 2
else:
    d = nails[0] - nails[n-1]
    f = 0
    for c in range(0, n-2):
        tmp = nails[c] - nails[c + 1]
        if d > tmp:
            d = tmp
            f = c
        c += 2
    while i in range(0, c):
        result += nails[i] - nails[i + 1]
        i += 2
    result += nails[c] - nails[c + 1]
    b = c
    while b in range(c, n-1):
        result += nails[b] - nails[b + 1]
        b += 2
print(result)
file = open('nails.out', 'w')
file.write(str(result))
file.close()