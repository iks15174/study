import sys
import math

input = sys.stdin.readline

ans = math.inf
ans_result = []
n = int(input().strip())
liquids = sorted(list(map(int, input().strip().split())))


def find_liquid(start, value):
    global n, liquids
    left = start
    right = n - 1
    prev_diff = math.inf
    ret = -1
    while left <= right:
        mid = (left + right) // 2
        diff = liquids[mid] + value
        if diff == 0:
            return mid
        if abs(diff) < prev_diff:
            ret = mid
            prev_diff = abs(diff)
        if diff > 0:
            right = mid - 1
        elif diff < 0:
            left = mid + 1
    return ret


for i in range(n - 2):
    for j in range(i + 1, n - 1, 1):
        third_liquid = find_liquid(j + 1, liquids[i] + liquids[j])
        total = liquids[i] + liquids[j] + liquids[third_liquid]
        if abs(total) < abs(ans):
            ans = abs(total)
            ans_list = [liquids[i], liquids[j], liquids[third_liquid]]

print(" ".join(map(str, ans_list)))
