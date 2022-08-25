import math
import heapq

def solution(n, paths, gates, summits):
    gates = set(gates)
    summits = set(summits)
    node_intensity = [math.inf] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for i, j, w in paths:
        graph[i].append([j, w])
        graph[j].append([i, w])
    q = []
    visited = [math.inf] * (n + 1)
    for g in gates:
        heapq.heappush(q, [0, g, g])
        visited[g] = 0
    while q:
        inten, node, start = heapq.heappop(q)
        if visited[node] < inten:
            continue
        if node in summits:
            node_intensity[node] = min(node_intensity[node], inten)
            continue
        if node in gates and node != start:
            continue
        for next_n, w in graph[node]:
            cost = max(w, inten)
            if visited[next_n] > cost:
                visited[next_n] = cost
                heapq.heappush(q, [cost, next_n, start])
                
    ans = sorted(enumerate(node_intensity), key = lambda x : (x[1], x[0]))
    return ans[0]