import bisect
n = int(input())
nums = list(map(int, input().split()))
dp = [nums[0]]
for n in nums:
    if dp[-1] < n:
        dp.append(n)
    else:
        idx = bisect.bisect_left(dp, n)
        dp[idx] = n
print(len(dp))