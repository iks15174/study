# n = int(input())
# dp = [[[-1] * (2 ** 11) for _ in range(100 + 1)] for _ in range(10)]
# mod = 1000000000


# def solve(length, used, prev_num):
#     global dp, mod, n
#     if n <= 9:
#         return 0

#     if length == 0:
#         while used > 0:
#             if used & 1 == 0:
#                 return 0
#             used = used >> 1
#         return 1

#     temp = 0
#     if prev_num - 1 >= 0:
#         new_used = used | (1 << (prev_num - 1))
#         if dp[prev_num - 1][length - 1][new_used] != -1:
#             dp[prev_num - 1][length - 1][new_used] %= mod
#             temp = dp[prev_num - 1][length - 1][new_used]
#         else:
#             dp[prev_num - 1][length - 1][new_used] = (
#                 solve(length - 1, new_used, prev_num - 1) % mod
#             )
#             temp = dp[prev_num - 1][length - 1][new_used]

#     if prev_num + 1 <= 9:
#         new_used = used | (1 << (prev_num + 1))
#         if dp[prev_num + 1][length - 1][new_used] != -1:
#             dp[prev_num + 1][length - 1][new_used] %= mod
#             temp += dp[prev_num + 1][length - 1][new_used]
#         else:
#             dp[prev_num + 1][length - 1][new_used] = (
#                 solve(length - 1, new_used, prev_num + 1) % mod
#             )
#             temp += dp[prev_num + 1][length - 1][new_used]
#     return temp


# not_used = 1 << 10
# ans = 0
# for i in range(1, 10):
#     new_used = not_used | (1 << i)
#     ans += solve(n - 1, new_used, i)
#     ans %= mod
# print(ans)

n = int(input())
dp = [[[0] * 10 for _ in range(2 ** 10)] for _ in range(n + 1)]
mod = 1000000000

for num in range(1, 10):
    dp[1][1 << num][num] = 1
    
for l in range(2, n + 1):
    for used in range(2 ** 10):
        for last in range(10):
            if used & 1 << last:
                if last - 1 >= 0:
                    dp[l][used][last] += (
                        dp[l - 1][used][last - 1]
                        + dp[l - 1][used & ~(1 << last)][last - 1]
                    )
                if last + 1 <= 9:
                    dp[l][used][last] += (
                        dp[l - 1][used][last + 1]
                        + dp[l - 1][used & ~(1 << last)][last + 1]
                    )
                dp[l][used][last] %= mod

ans = 0
for last in range(10):
    ans += dp[n][2 ** 10 - 1][last]
    ans %= mod
print(ans)
