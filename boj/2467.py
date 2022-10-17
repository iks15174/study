# import math

# n = int(input())
# liquids = list(map(int, input().split()))
# start = 0
# end = n - 1
# ans_start = start
# ans_end = end
# cand = math.inf
# while start < end:
#     sum = liquids[start] + liquids[end]
#     if abs(sum) < abs(cand):
#         cand = sum
#         ans_start = start
#         ans_end = end
#     if sum > 0:
#         end -= 1
#     elif sum < 0:
#         start += 1
#     else:
#         break

# print(liquids[ans_start], liquids[ans_end])

import bisect

n = int(input())
liquids = list(map(int, input().split()))
ans = [liquids[0], liquids[1]]
val = abs(liquids[0] + liquids[1])
for idx, l in enumerate(liquids):
    new_idx = bisect.bisect_left(liquids, -l)
    if new_idx == len(liquids):
        new_idx -= 1
    if (not new_idx == idx) and abs(liquids[new_idx] + l) < val:
        val = abs(liquids[new_idx] + l)
        ans = [liquids[new_idx], l]
    if (not new_idx - 1 == idx) and new_idx - 1 >= 0 and abs(liquids[new_idx - 1] + l) < val:
        val = abs(liquids[new_idx - 1] + l)
        ans = [liquids[new_idx - 1], l]
    if (not new_idx + 1 == idx) and new_idx + 1 < len(liquids) and abs(liquids[new_idx + 1] + l) < val:
        val = abs(liquids[new_idx + 1] + l)
        ans = [liquids[new_idx + 1], l]
    
print(' '.join(map(str, sorted(ans))))



