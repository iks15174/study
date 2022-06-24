import sys
from collections import deque
import math

input = sys.stdin.readline
n = int(input().strip())
ants = []
road = [[] for _ in range(n)]
dist = [0] * n
start = 0
for _ in range(n):
    ants.append(int(input().strip()))
    
for _ in range(n -1):
    a, b, c = map(int, input().strip().split())
    a -= 1
    b -= 1
    road[a].append([b, c])
    road[b].append([a, c])
    
q = deque([[start, 0]])
visited = [False] * n
visited[0] = True
while q:
    node, cost = q.popleft()
    for np, c in road[node]:
        if not visited[np]:
            dist[np] = cost + c
            visited[np] = True
            q.append([np, c + cost])

for i in range(n):
    if ants[i] >= dist[i]:
        print(1)
    else:
        energy = ants[i]
        cur_pos = i
        while energy < dist[cur_pos]:
            for nx, c in road[cur_pos]:
                if dist[nx] < dist[cur_pos]:
                    if energy >= c:
                        energy -= c
                        cur_pos = nx
                    else:
                        energy = math.inf
                    break
        print(cur_pos + 1)