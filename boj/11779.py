import sys
import math
import heapq

input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())
graph = [[] for _ in range(n + 1)]
dist = [math.inf] * (n + 1)
prev = [0] * (n + 1)

for _ in range(m):
    start, end, dis = map(int, input().strip().split())
    graph[start].append((end, dis))
start, end = map(int, input().strip().split())

q = []
prev[start] = start
dist[start] = 0
heapq.heappush(q, (0, start))
while q:
    dis, node = heapq.heappop(q)
    if dist[node] < dis:
        continue
    for next_node, next_dist in graph[node]:
        cost = dist[node] + next_dist
        if cost < dist[next_node]:
            dist[next_node] = cost
            prev[next_node] = node
            heapq.heappush(q, (cost, next_node))

path = [end]
cur = end
while cur != start:
    path.append(prev[cur])
    cur = prev[cur]
print(dist[end])
print(len(path))
print(" ".join(map(str, reversed(path))))
