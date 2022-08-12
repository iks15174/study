import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
depen = [[] for _ in range(n + 1)]
depenn = [0] * (n + 1)
for _ in range(m):
    prev, next = map(int, input().split())
    depen[prev].append(next)
    depenn[next] += 1
    
cand = []
for i in range(1, n + 1):
    if depenn[i] == 0:
        heapq.heappush(cand, i)

ans = []
while cand:
    cur = heapq.heappop(cand)
    ans.append(str(cur))
    for nx in depen[cur]:
        depenn[nx] -= 1
        if depenn[nx] == 0:
            heapq.heappush(cand, nx)
            
print(" ".join(ans))