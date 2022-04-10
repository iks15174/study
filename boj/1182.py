n, s = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = 0


def solve(idx, sum):
    global ans
    if idx >= len(nums):
        return

    sum += nums[idx]
    if sum == s:
        ans += 1

    solve(idx + 1, sum)
    solve(idx + 1, sum - nums[idx])


solve(0, 0)
print(ans)
