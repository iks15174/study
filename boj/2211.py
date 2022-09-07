from dis import dis
import sys
import heapq
import math

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append([b, w])
    graph[b].append([a, w])
    
q = [[0, 1, []]]
dist = [math.inf] * (n + 1)
dist[1] = 0
result = []
while q:
    d, node, connection = heapq.heappop(q)
    if dist[node] < d:
        continue
    result.append(connection)
    for nn, nw in graph[node]:
        cost = nw + d
        if dist[nn] > cost:
            dist[nn] = cost
            heapq.heappush(q, [cost, nn, [node, nn]])
            

print(len(result) - 1)
for r in result:
    if len(r) == 0:
        continue
    print(str(r[0]) + ' ' + str(r[1]))