from itertools import combinations
from collections import deque
import copy

n, m = list(map(int, input().split()))
graph = []
zeros = []
twos = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if line[j] == 0:
            zeros.append((i, j))
        elif line[j] == 2:
            twos.append((i, j))
    graph.append(line)
wallPosComb = list(combinations(zeros, 3))

def bfs(combs):
    global n, m, graph, twos
    gcopy = copy.deepcopy(graph)
    for c in combs:
        cx, cy = c
        gcopy[cx][cy] = 1
    q = deque(copy.deepcopy(twos))
    cnt = len(zeros) - 3
    while q:
        px, py = q.popleft()
        ns = [(px-1, py), (px+1, py), (px, py-1), (px, py+1)]
        for np in ns:
            nx, ny = np
            if n > nx >= 0 and m > ny >= 0 and gcopy[nx][ny] == 0:
                gcopy[nx][ny] = 2
                q.append((nx, ny))
                cnt -= 1
    # cnt= 0
    # for line in gcopy:
    #     for j in line:
    #         if j==0:
    #             cnt += 1
    return cnt

maxval = 0
for comb in wallPosComb:
    maxval = max(maxval, bfs(comb))
print(maxval)
