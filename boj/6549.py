import math


def histogram(nums):
    s = []
    ans = -math.inf
    for i in range(len(nums)):
        while s and s[-1][0] > nums[i]:
            bar, idx = s.pop()
            w = i
            if s:
                w -= s[-1][1] + 1
            ans = max(ans, w * bar)
        s.append([nums[i], i])

    while s:
        bar, idx = s.pop()
        w = len(nums)
        if s:
            w -= s[-1][1] + 1
        ans = max(ans, w * bar)
    print(ans)


while True:
    nums = list(map(int, input().split()))
    if len(nums) == 1 and nums[0] == 0:
        break
    histogram(nums[1:])
