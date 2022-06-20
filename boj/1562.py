import sys

n = int(input())
dp = [[[-1] * (2 ** 11) for _ in range(100 + 1)] for _ in range(10)]
mod = 1000000000


def solve(length, used, prev_num):
    global dp, mod, n
    if n <= 9:
        return 0

    if length == 0:
        while used > 0:
            if used & 1 == 0:
                return 0
            used = used >> 1
        return 1

    temp = 0
    if prev_num - 1 >= 0:
        new_used = used | (1 << (prev_num - 1))
        if dp[prev_num - 1][length - 1][new_used] != -1:
            dp[prev_num - 1][length - 1][new_used] %= mod
            temp = dp[prev_num - 1][length - 1][new_used]
        else:
            dp[prev_num - 1][length - 1][new_used] = (
                solve(length - 1, new_used, prev_num - 1) % mod
            )
            temp = dp[prev_num - 1][length - 1][new_used]

    if prev_num + 1 <= 9:
        new_used = used | (1 << (prev_num + 1))
        if dp[prev_num + 1][length - 1][new_used] != -1:
            dp[prev_num + 1][length - 1][new_used] %= mod
            temp += dp[prev_num + 1][length - 1][new_used]
        else:
            dp[prev_num + 1][length - 1][new_used] = (
                solve(length - 1, new_used, prev_num + 1) % mod
            )
            temp += dp[prev_num + 1][length - 1][new_used]
    return temp


not_used = 1 << 10
ans = 0
for i in range(1, 10):
    new_used = not_used | (1 << i)
    ans += solve(n - 1, new_used, i)
    ans %= mod
print(ans)
