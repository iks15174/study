import sys
import math

input = sys.stdin.readline
n, m , r = map(int, input().split())
items = list(map(int, input().split()))
graph = [[math.inf] * n for _ in range(n)]
for _ in range(r):
    a, b, d = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], d)
    graph[b-1][a-1] = min(graph[b-1][a-1], d)
for i in range(n):
    graph[i][i] = 0

for middle in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][middle] + graph[middle][j])    
            
ans = 0
for start in range(n):
    cur_dist = graph[start]
    cnt = 0
    for idx, cd in enumerate(cur_dist):
        if cd <= m:
           cnt += items[idx]
    ans = max(ans, cnt)
print(ans)  