import sys

sys.setrecursionlimit(10 ** 9)
nums = list(map(int, input().split()))
nums.pop()  # 마지막 0 제거
# dp[l][r][task] l, r에 있고 task번째 task를 할 때 마지막까지 사용하는 힘의 최솟값을 의미
dp = [[[0] * 5 for _ in range(5)] for _ in range(len(nums))]


def move(fr, to):
    if fr == to:
        return 1
    if fr == 0 or to == 0:
        return 2
    if (fr == 2 and to == 4) or (fr == 4 and to == 2):
        return 4
    if (fr == 3 and to == 1) or (fr == 1 and to == 3):
        return 4
    else:
        return 3


def solve(l, r, task):
    global nums, dp
    if task == len(nums):
        return 0
    if dp[task][l][r] != 0:
        return dp[task][l][r]

    dp[task][l][r] = min(
        move(l, nums[task]) + solve(nums[task], r, task + 1),
        move(r, nums[task]) + solve(l, nums[task], task + 1),
    )

    return dp[task][l][r]


solve(0, 0, 0)
print(dp[0][0][0])
