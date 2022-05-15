import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
n = int(input().strip())
nums = list(map(int, input().strip().split()))
question = int(input().strip())

# dp[i][j] 는 i ~ j까지의 수가 펠린드롬인지의 여부를 의미한다.
dp = [[-1] * (n + 1) for _ in range(n + 1)]


def make_pedlindorm(i, j):
    global nums, dp
    if i == j:
        dp[i][j] = 1
    elif abs(i - j) == 1:
        if nums[i - 1] == nums[j - 1]:
            dp[i][j] = 1
        else:
            dp[i][j] = 0
    else:
        if dp[i][j] == -1:
            is_pelin = make_pedlindorm(i + 1, j - 1)
            if is_pelin and (nums[i - 1] == nums[j - 1]):
                dp[i][j] = 1
            else:
                dp[i][j] = 0
    return dp[i][j]


for i in range(1, n + 1):
    for j in range(i, n + 1):
        make_pedlindorm(i, j)
for _ in range(question):
    s, e = map(int, input().strip().split())
    print(dp[s][e])
