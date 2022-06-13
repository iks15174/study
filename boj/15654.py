n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
used = [False] * n


def solve(arr, length):
    global nums, used
    if length == 0:
        print(" ".join(map(str, arr)))
    else:
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                arr.append(nums[i])
                solve(arr, length - 1)
                used[i] = False
                arr.pop()


solve([], m)
