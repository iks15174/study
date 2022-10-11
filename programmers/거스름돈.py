def solution(n, money):
    dp = [0] * (n + 1)
    dp[0] = 1
    for m in money:
        for i in range(1, n + 1):
            if i - m >= 0:
                dp[i] += dp[i - m]
                dp[i] %= 1000000007
    return dp[n] % 1000000007