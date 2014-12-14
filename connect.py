__author__ = 'rezenter'
file = open('connect.in', 'r')
n = file.readline().split()
n, m = int(n[0]), int(n[1])
pairs = []
i = 0
while i != m:
    i += 1
    pairs.append(list(file.readline()))
file.close()
g = [[0] * n for i in range(n)]
print(g)
start = [0] * n
stop = [0] * n
for i in pairs:
    g[int(i[0]) - 1][int(i[2]) - 1] = 1
    g[int(i[2]) - 1][int(i[0]) - 1] = 1
ex = set()
print(g)

def dfs(node):
    global clock
    start[node] = clock
    ex.add(node)
    clock += 1
    for i in range(len(g)):
        if g[node][i] == 1 and i not in ex:
            dfs(i)
            clock += 1
    stop[node] = clock
clock = 0
count = 0
relation = [1] * n
visited = [None] * n
for i in range(len(g[0])):
    if i not in ex:
        count += 1
        dfs(i)
        stop[i] = clock
        for v in range(n):
            if v in ex and visited[v] is None:
                relation[v] = count
                visited[v] = 0
file = open('connect.out', 'w')
file.write(str(count) + '\n')
print(count)
while len(relation) > 1:
    file.write(str(relation.pop(0)) + ' ')
file.write(str(relation.pop(0)))
file.close()