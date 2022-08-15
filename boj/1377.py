import sys

input = sys.stdin.readline
n = int(input())
nums = [(int(input()), i) for i in range(n)]
sorted_nums = sorted(nums)
ans = 0
for i in range(n):
    ans = max(ans, sorted_nums[i][1] - i)
print(ans + 1)