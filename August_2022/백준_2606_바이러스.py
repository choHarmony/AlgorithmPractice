import sys

comNum = int(sys.stdin.readline())
network = int(sys.stdin.readline())
graph = []

for i in range(network) :
    a, b = map(int, sys.stdin.readline().split())
    graph.append([a, b])

def dfs(graph, start, visited = []) :
    visited.append(start)

    for i in range(len(graph)) :
        for node in graph[i] :
            if node not in visited and start in graph[i]:
                dfs(graph, node, visited)

    return visited

print(len(dfs(graph, 1))-1)