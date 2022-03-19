n = int(input())
nums = list(map(int, input().split()))
nums_pos = [-1] * 1000001
ans = 0
for idx, num in enumerate(nums):
    nums_pos[num] = idx
# dp[i][j]는 j를 마지막 항, i를 이전의 항으로 갖는 연속된 3이상 수열의 최댓값이다.
dp = [[0] * n for _ in range(n)]

# 기본으로 연속된 세개의 수를 dp에 초기화 시켜준다.
for i in range(n - 1):
    for j in range(i + 1, n):
        interval = nums[j] - nums[i]
        prev = nums[i] - interval
        if prev >= 0 and nums_pos[prev] != -1:  # prev, nums[i], nums[j] 가 존재하면
            dp[i][j] = prev + nums[j] + nums[i]
            ans = max(ans, dp[i][j])

for i in range(n - 1):
    for j in range(i + 1, n):
        if dp[i][j]:
            interval = nums[j] - nums[i]
            prev = nums[i] - interval
            if prev >= 0 and nums_pos[prev] != -1:  # prev, nums[i], nums[j] 가 존재하면
                dp[i][j] = max(dp[i][j], dp[nums_pos[prev]][i] + nums[j])
                ans = max(ans, dp[i][j])


print(ans)
