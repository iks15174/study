import math
import sys
import heapq

input = sys.stdin.readline
n, m, k = map(int, input().split())
dp = [[math.inf] * (k + 1) for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    c1, c2, cost = map(int, input().split())
    graph[c1].append([c2, cost])
    graph[c2].append([c1, cost])

q = []
dp[1][0] = 0
heapq.heappush(q, [0, 1, 0]) # cost, node, 포장횟수
while q:
    cost, node, used_k = heapq.heappop(q)
    if dp[node][used_k] < cost:
        continue
    for nn, nnw in graph[node]:
        nn_cost = nnw + cost
        if nn_cost < dp[nn][used_k]:
            dp[nn][used_k] = nn_cost
            heapq.heappush(q, [nn_cost, nn, used_k])
        if used_k < k and cost < dp[nn][used_k + 1]:
            dp[nn][used_k + 1] = cost
            heapq.heappush(q, [cost, nn, used_k + 1])
            

print(min(dp[n]))
