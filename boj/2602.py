magic = list(input())
devil = list(input())
angel = list(input())

# dp[i][j][k] => 지금까지 사용한 최대 인덱스가 i이고, 찾아야 하는 magic index가 j이고, k 방향(0:악마, 1:천사)일 때 가능한 가짓수를 저장한다.
dp = [[[-1] * 2 for _ in range(len(magic))] for _ in range(len(angel))]

# 현재까지 사용한 idx, 찾아야하는 magic_idx, order = 1 천사차례, 0은 악마차례
def solve(last_idx, magic_idx, order):
    if magic_idx == len(magic):
        return 1
    if dp[last_idx][magic_idx][order] != -1:
        return dp[last_idx][magic_idx][order]

    ans = 0
    if order == 0:
        for idx, d in enumerate(devil):
            if d == magic[magic_idx] and idx > last_idx:
                ans += solve(idx, magic_idx + 1, 1 - order)
    if order == 1:
        for idx, a in enumerate(angel):
            if a == magic[magic_idx] and idx > last_idx:
                ans += solve(idx, magic_idx + 1, 1 - order)
    dp[last_idx][magic_idx][order] = ans
    return ans


print(solve(-1, 0, 1) + solve(-1, 0, 0))
