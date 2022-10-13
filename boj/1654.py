# import sys

# input = sys.stdin.readline
# k, n = map(int, input().strip().split())
# lansun = []
# left = 1
# right = -1
# for _ in range(k):
#     new_lansun = int(input().strip())
#     right = max(right, new_lansun)
#     lansun.append(new_lansun)


# def calculate_lan_num(lansum_length):
#     result = 0
#     for lan in lansun:
#         result += lan // lansum_length
#     return result


# # upper bound 구한 후 -1한다.
# right += 1
# while left < right:
#     mid = (left + right) // 2  # 중간길이
#     splitted_lan = calculate_lan_num(mid)

#     if splitted_lan == n:
#         left = mid + 1
#     elif splitted_lan > n:
#         left = mid + 1
#     elif splitted_lan < n:
#         right = mid

# print(left - 1)

import sys

input = sys.stdin.readline
k, n = map(int, input().split())
lansuns = [int(input()) for _ in range(k)]
left = 1
right = max(lansuns) + 1
ans = -1
while left < right:
    mid = (left + right) // 2
    new_cnt = 0
    for l in lansuns:
        new_cnt += (l // mid)
    if new_cnt >= n:
        left = mid + 1
    else:
        right = mid
print(right - 1)
