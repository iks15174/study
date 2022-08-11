n, k = map(int, input().split())
mod = 1000000000
dp = [[0] * (n + 1) for _ in range(k + 1)]
for i in range(1, k + 1):
    dp[i][0] = 1

for num in range(1, n + 1):
    dp[1][num] = 1
    
for num in range(1, n + 1):
    for ki in range(2, k + 1):
        for i in range(n + 1):
            if num - i >= 0:
                dp[ki][num] += (dp[ki - 1][num - i] % mod)
                    
print(dp[k][n] % mod)