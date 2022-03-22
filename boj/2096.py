import sys

input = sys.stdin.readline
n = int(input().strip())
min_dp = [[0] * 3, [10e8] * 3]
max_dp = [[0] * 3 for _ in range(2)]
table = []

for _ in range(n):
    table = list(map(int, input().strip().split()))
    for j in range(3):
        max_dp[1][j] = max(max_dp[1][j], max_dp[0][j] + table[j])
        min_dp[1][j] = min(min_dp[1][j], min_dp[0][j] + table[j])

        if j - 1 >= 0:
            max_dp[1][j] = max(max_dp[1][j], max_dp[0][j - 1] + table[j])
            min_dp[1][j] = min(min_dp[1][j], min_dp[0][j - 1] + table[j])
        if j + 1 < 3:
            max_dp[1][j] = max(max_dp[1][j], max_dp[0][j + 1] + table[j])
            min_dp[1][j] = min(min_dp[1][j], min_dp[0][j + 1] + table[j])

    # 현재값을 이전 값으로 변경한다.
    max_dp[0] = max_dp[1]
    min_dp[0] = min_dp[1]
    max_dp[1] = [0, 0, 0]
    min_dp[1] = [10e8, 10e8, 10e8]

print(
    max(max_dp[0][0], max_dp[0][1], max_dp[0][2]),
    min(min_dp[0][0], min_dp[0][1], min_dp[0][2]),
)
