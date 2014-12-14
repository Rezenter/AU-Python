__author__ = 'rezenter'
file = open('dfsongrid.in', 'r')
n = file.readline().split()
n, m, x1, y1, x2, y2 = int(n[0]), int(n[1]), int(n[2]), int(n[3]), int(n[4]), int(n[5])
g = [[0] * n for i in range(m)]
i = 0
while i != m:
    j = 0
    tmp = file.readline()
    while j != n:
        if tmp[j] == '.':
            t = True
        else:
            t = False
        g[i][j] = t
        j += 1
    i += 1
file.close()
ex = set()


def dfs(node):
    ex.add(node)
    for i in range(len(g)):
        if g[node][i] == 1 and i not in ex:
            dfs(i)
relation = [1] * n
visited = [None] * n
for i in range(len(g[0])):
    if i not in ex:
        dfs(i)
        for v in range(n):
            if v in ex and visited[v] is None:
                visited[v] = 0

file = open('dfsongrid.out', 'w')

file.close()