import math
import heapq

"""
풀이
1 -> N으로 가는 최단경로를 구하는 문제이기 때문에 다익스트라 알고리즘으로 접근한다.
단 x, y를 반드시 거쳐야 한다.
나올 수 있는 경우의 수는 1 -> x -> y -> N 이거나 1 -> y -> x -> N이다.
각각의 최단 경로를 다익스타라 알고리즘을 이용해 구하면 된다.
"""
n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

x, y = map(int, input().split())

# start에서 시작해서 각 정점으로 가는 최단거리를 구하는 함수이다.
def dijkstra(start, target):
    global n, graph
    dist = [math.inf] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        dis, node = heapq.heappop(q)
        if dist[node] < dis:
            continue
        for to, to_dist in graph[node]:
            cost = to_dist + dist[node]
            if cost < dist[to]:
                dist[to] = cost
                heapq.heappush(q, (cost, to))

    result = []
    for t in target:
        result.append(dist[t])
    return result


to_x, to_y = dijkstra(1, [x, y])
ans = min(
    to_x + dijkstra(x, [y])[0] + dijkstra(y, [n])[0],
    to_y + dijkstra(y, [x])[0] + dijkstra(x, [n])[0],
)
if ans == math.inf:
    print(-1)
else:
    print(ans)
