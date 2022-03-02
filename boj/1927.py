import heapq
import sys

input = sys.stdin.readline

n = int(input())
queue = []
for _ in range(n):
    num = int(input())
    if num == 0:
        try:
            print(heapq.heappop(queue))
        except IndexError:
            print(0)
    else:
        heapq.heappush(queue, num)
