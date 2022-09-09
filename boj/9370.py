import heapq
import sys
import math

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, m, tt = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        if sorted([a, b]) == sorted([g, h]):
            d -= 0.1
        graph[a].append([b, d])
        graph[b].append([a, d])
    target_cand = []
    for _ in range(tt):
        target_cand.append(int(input()))
        
    dist = [math.inf] * (n + 1)
    dist[s] = 0
    q = []
    heapq.heappush(q, [0, s, False])
    ans = set()
    while q:
        nd, node, passed = heapq.heappop(q)
        if dist[node] < nd:
            continue
        if passed and node in target_cand:
            ans.add(node)
        for nn, nnd in graph[node]:
            cost = nnd + nd
            if cost < dist[nn]:
                dist[nn] = cost
                new_passed = passed
                if sorted([nn, node]) == sorted([h, g]):
                    new_passed = True
                heapq.heappush(q, [cost, nn, new_passed])
                
                
    print(' '.join(map(str, sorted(list(ans)))))
            
        