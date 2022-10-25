import math
import heapq

def solution(n, roads, sources, destination):
    dist = [math.inf] * n
    graph = [[] for _ in range(n)]
    for s, e in roads:
        s -= 1
        e -= 1
        graph[s].append(e)
        graph[e].append(s)
    dist[destination - 1] = 0
    q = []
    heapq.heappush(q, [0, destination - 1])
    while q:
        cdist, node = heapq.heappop(q)
        if cdist > dist[node]:
            continue
        for nnode in graph[node]:
            cost = cdist + 1
            if dist[nnode] > cost:
                dist[nnode] = cost
                heapq.heappush(q, [cost, nnode])
    ans = []
    for s in sources:
        if dist[s - 1] != math.inf:
            ans.append(dist[s - 1])
        else:
            ans.append(-1)
    return ans