import sys
import math

input = sys.stdin.readline

n = int(input().strip())
# dp[i][j]는 i ~ j 매트릭스 곱의 최솟값을 의미한다.
dp = [[0] * (n + 1) for _ in range(n + 1)]
mat_mul = []
for _ in range(n):
    a, b = map(int, input().strip().split())
    mat_mul.append([a, b])

for interval in range(2, n + 1):
    for start in range(1, n - interval + 2):
        last = start + interval - 1
        if interval == 2:
            dp[start][last] = (
                mat_mul[start - 1][0] * mat_mul[start - 1][1] * mat_mul[last - 1][1]
            )
        else:
            ans = math.inf
            for mid in range(start, last):
                ans = min(
                    ans,
                    dp[start][mid]
                    + dp[mid + 1][last]
                    + mat_mul[start - 1][0]
                    * mat_mul[mid - 1][1]
                    * mat_mul[last - 1][1],
                )
            dp[start][last] = ans

print(dp[1][n])
