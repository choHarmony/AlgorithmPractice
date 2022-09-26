from collections import deque

n, m = map(int, input().split()) # 학생 수, 키를 비교한 횟수
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m) :
    s, e = map(int, input().split())
    graph[s].append(e)
    indegree[e] += 1

def t_sort() :
    res = []
    q = deque()
    for i in range(1, n+1) :
        if indegree[i] == 0 :
            q.append(i)

    while q :
        node = q.popleft()
        res.append(node)
        for next in graph[node] :
            indegree[next] -= 1
            if indegree[next] == 0 :
                q.append(next)
    for i in res :
        print(i, end=' ')

t_sort()