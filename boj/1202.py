# import heapq
# import sys

# input = sys.stdin.readline

# n, k = map(int, input().split())
# gem_weight_value = []
# bags = []

# # 보석의 무게, 가격 정보와 가방 용량 정보를 입력받는다.
# for _ in range(n):
#     gem_weight_value.append(list(map(int, input().split())))
# for _ in range(k):
#     bags.append(int(input()))

# # 각 가방의 최대한의 가치를 지닌 보석을 넣으면 된다.
# sorted_gem = sorted(gem_weight_value, key=lambda item: item[0])
# sorted_bags = sorted(bags)
# gem_index = 0
# gem_queue = []
# result = 0

# for bag in sorted_bags:
#     while (
#         gem_index < int(n) and sorted_gem[gem_index][0] <= bag
#     ):  # 현재 가방 사이즈에 가능한 보석들을 힙큐에 넣어둔다.
#         heapq.heappush(gem_queue, -sorted_gem[gem_index][1])
#         gem_index += 1
#     if len(gem_queue) > 0:
#         result += -heapq.heappop(gem_queue)

# print(result)

import sys
from collections import deque
import heapq

input = sys.stdin.readline
n, k = map(int, input().split())
jewl = deque(sorted([list(map(int, input().split())) for _ in range(n)]))
bags = sorted([int(input()) for _ in range(k)])

q = []
ans = 0
for b in bags:
    while jewl:
        if jewl[0][0] <= b:
            heapq.heappush(q, -jewl[0][1])
            jewl.popleft()
        else:
            break
    if q:
        ans += (-heapq.heappop(q))
print(ans)
