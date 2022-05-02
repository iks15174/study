import heapq
import sys

input = sys.stdin.readline

n = int(input().strip())
planks = []
for _ in range(n):
    plank = int(input().strip())
    heapq.heappush(planks, plank)

ans = 0
for _ in range(n - 1):
    first = heapq.heappop(planks)
    second = heapq.heappop(planks)
    ans += first + second
    heapq.heappush(planks, first + second)

print(ans)
