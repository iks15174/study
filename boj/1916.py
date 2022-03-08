import math
import heapq
import sys

input = sys.stdin.readline

v_len = int(input().strip())
e_len = int(input().strip())
distance = [math.inf] * v_len
edges = [[] for _ in range(v_len)]  # 간선의 정보를 담고 있다
for _ in range(e_len):
    v1, v2, value = map(int, input().strip().split())
    edges[v1 - 1].append([v2 - 1, value])  # v1 -> v2로 갈때 value만큼 든다는 정보를 저장한다.

start, target = map(int, input().strip().split())  # 시작점, 끝점
start = start - 1
target = target - 1

queue = []
heapq.heappush(
    queue,
    [0, start],
)  # node와 value를 저장한다.
distance[start] = 0

while queue:
    dist, node = heapq.heappop(queue)
    if distance[node] < dist:
        continue
    for next_node_info in edges[node]:
        next_node, next_dist = next_node_info
        cost = next_dist + dist
        if cost < distance[next_node]:
            distance[next_node] = cost
            heapq.heappush(queue, [cost, next_node])

print(distance[target])
