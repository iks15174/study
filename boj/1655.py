import heapq
import sys

input = sys.stdin.readline
minq = []
maxq = []
n = int(input().strip())
for i in range(n):
    new_n = int(input().strip())
    if len(minq) == len(maxq):
        if len(maxq) == 0:
            heapq.heappush(maxq, -new_n)
        else:
            if new_n > minq[0]:
                temp = heapq.heappop(minq)
                heapq.heappush(maxq, -temp)
                heapq.heappush(minq, new_n)
            else:
                heapq.heappush(maxq, -new_n)
    else:
        if new_n < -maxq[0]:
            temp = -heapq.heappop(maxq)
            heapq.heappush(minq, temp)
            heapq.heappush(maxq, -new_n)
        else:
            heapq.heappush(minq, new_n)

    print(-maxq[0])
