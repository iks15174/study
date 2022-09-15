import sys
import heapq

input = sys.stdin.readline
n = int(input())
cup_ramen = []
for _ in range(n):
    deadline, reward = map(int, input().split())
    cup_ramen.append([reward, deadline])
cup_ramen = sorted(cup_ramen, key= lambda x : x[1])
q = []
for r, d in cup_ramen:
    while q and len(q) >= d and q[0] < r:
        heapq.heappop(q)
    if len(q) < d:
        heapq.heappush(q, r)
print(sum(q))