from dis import dis
import heapq
import sys
import math

input = sys.stdin.readline
n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
graphr = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, d = map(int, input().split())
    graph[a].append([b, d])
    graphr[b].append([a, d])
    
dist = [math.inf] * (n + 1)
distr = [math.inf] * (n + 1)
q = [[0, x]]
dist[0] = 0
dist[x] = 0
while q:
    d, node = heapq.heappop(q)
    if dist[node] < d:
        continue
    for nn, nnd in graph[node]:
        cost = nnd + d
        if cost < dist[nn]:
            dist[nn] = cost
            heapq.heappush(q, [cost, nn])    
            
            
q = [[0, x]]
distr[0] = 0
distr[x] = 0
while q:
    d, node = heapq.heappop(q)
    if distr[node] < d:
        continue
    for nn, nnd in graphr[node]:
        cost = nnd + d
        if cost < distr[nn]:
            distr[nn] = cost
            heapq.heappush(q, [cost, nn])    
            
ans = -1
for pd, rd in zip(dist, distr):
    ans = max(ans, pd + rd)
print(ans)