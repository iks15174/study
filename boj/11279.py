import heapq
import sys

input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    op = int(input())
    if op == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(-heapq.heappop(arr))
    else:
        heapq.heappush(arr, -op)
