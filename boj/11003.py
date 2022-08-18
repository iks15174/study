import heapq
import sys

input = sys.stdin.readline
n, l = map(int, input().split())
nums = list(map(int, input().split()))
l_list = []
for idx, ns in enumerate(nums):
    if len(l_list) < l:
        heapq.heappush(l_list, (ns, idx))
        print(l_list[0][0], end= " ")
    else:
        heapq.heappush(l_list, (ns, idx))
        c_left = idx - l + 1
        c_right = idx
        while l_list[0][1] < c_left:
            heapq.heappop(l_list)
        print(l_list[0][0], end= " ")