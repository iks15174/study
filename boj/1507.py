import heapq
import sys
import math

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
distq = []
for r in range(n - 1):
    for c in range(r + 1, n):
        heapq.heappush(distq, [board[r][c], r, c])

def dikstra(n, s, e, graph):
    dist = [math.inf] * n
    dist[s] = 0
    q = []
    heapq.heappush(q, [0, s])
    while q:
        cur_dist, node = heapq.heappop(q)
        if cur_dist > dist[node]:
            continue
        for nnode, w in graph[node]:
            cost = w + cur_dist
            if cost < dist[nnode]:
                dist[nnode] = cost
                heapq.heappush(q, [cost, nnode])
    return dist[e]
graph = [[] for _ in range(n)]
ans = 0
while distq:
    dist, s, e = heapq.heappop(distq)
    s_to_e = dikstra(n, s, e, graph)
    if s_to_e > dist:
        graph[s].append([e, dist])
        graph[e].append([s, dist])
        ans += dist
    elif s_to_e < dist:
        print(-1)
        sys.exit()
        
print(ans)
    