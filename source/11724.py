n, m = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for i in range(m):
    fr, t = list(map(int, input().split()))
    if t not in graph[fr]:
        graph[fr].append(t)
    if fr not in graph[t]:
        graph[t].append(fr)

def dfs(graph, node, visited):
    for n in graph[node]:
        if visited[n]:
            continue
        visited[n] = True
        dfs(graph, n, visited)


conns = 0
visited = [False for _ in range(n + 1)]
for i in range(1, n + 1):
    if visited[i]:
        continue
    visited[i] = True
    dfs(graph, i, visited)
    conns += 1
print(conns)
