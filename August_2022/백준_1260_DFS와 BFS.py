def funcdfs(v) :
    visited[v] = 1
    dfs.append(v)
    for i in graph[v] :
        if (visited[i] == 0) :
            funcdfs(i)

def funcbfs(v) :
    visited[v] = 1
    bfs.append(v)
    queue = [v]

    while queue :
        for i in graph[queue.pop(0)] :
            if visited[i] == 0 :
                visited[i] = 1
                bfs.append(i)
                queue.append(i)

import sys

n, m, v = map(int, sys.stdin.readline().split()) # 정점 개수, 간선 개수, 탐색 시작할 정점의 번호
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
dfs = []
bfs = []

for i in range(m) :
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

for i in range(n+1) :
    graph[i].sort()
funcdfs(v)

for j in range(n+1) :
    visited[j] = 0
funcbfs(v)

for i in dfs :
    print(i, end=' ')
print()
for i in bfs :
    print(i, end=' ')