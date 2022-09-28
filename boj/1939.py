import sys
from collections import deque
import math

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [dict() for _ in range(n + 1)]
for _ in range(m):
    s, e, c = map(int, input().split())
    if e in graph[s]:
        graph[s][e] = max(graph[s][e], c)
    else:
        graph[s][e] = c
    if s in graph[e]:
        graph[e][s] = max(graph[e][s], c)
    else:
        graph[e][s] = c
start, end = map(int, input().split())
visited = [0] * (n + 1)
q = deque([[start, math.inf]])
visited[start] = math.inf
ans = -1
while q:
    node, max_load = q.popleft()
    if node == end:
        ans = max(ans, max_load)
        continue
    for nn, load in graph[node].items():
        cur_load = min(max_load, load)
        if visited[nn] < cur_load:
            visited[nn] = cur_load
            q.append([nn, cur_load])
            
print(ans)