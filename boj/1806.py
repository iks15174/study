import math

n, s = map(int, input().split())
nums = list(map(int, input().split()))
front = 0
end = 0
min_len = math.inf
acc_sum = nums[0]

while True:
    if acc_sum < s:
        end += 1
        if end >= n:
            break
        acc_sum += nums[end]
    else:
        min_len = min(min_len, end - front + 1)
        acc_sum -= nums[front]
        front += 1
        if front > end:
            break

print(0 if min_len == math.inf else min_len)
