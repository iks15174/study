import sys
import math

input = sys.stdin.readline

v, e = map(int, input().strip().split())
edges = []
shortest_path = [[math.inf] * v for _ in range(v)]
for _ in range(e):
    s, e, l = map(int, input().strip().split())
    s -= 1
    e -= 1
    edges.append([s, e, l])
    shortest_path[s][e] = min(shortest_path[s][e], l)
    shortest_path[e][s] = min(shortest_path[e][s], l)


for i in range(v):
    for j in range(v):
        if i == j:
            shortest_path[i][j] = 0

for k in range(v):
    for i in range(v):
        for j in range(v):
            shortest_path[i][j] = min(
                shortest_path[i][j], shortest_path[i][k] + shortest_path[k][j]
            )

ans = math.inf
for i in range(v):
    ignit_time = [0] * v
    for j in range(v):
        ignit_time[j] = shortest_path[i][j]

    temp_ans = max(shortest_path[i])
    print(temp_ans)
    for e in edges:
        start = e[0]
        end = e[1]
        length = e[2]
        diff = abs(ignit_time[start] - ignit_time[end])
        burn_time = diff + (length - diff) / 2 + min(ignit_time[start], ignit_time[end])
        temp_ans = max(temp_ans, burn_time)

    ans = min(ans, temp_ans)

print(ans)
