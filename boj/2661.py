import sys

n = int(input())


def is_bad_nums(nums, length):
    mid = len(nums) - length
    if nums[mid:] == nums[len(nums) - 2 * length : mid]:
        return True
    return False


def solve(nums):
    global n
    if len(nums) == n:
        is_bad_num = False
        for i in range(1, len(nums) // 2 + 1):
            if is_bad_nums(nums, i):
                is_bad_num = True

        if not is_bad_num:
            print("".join(map(str, nums)))
            sys.exit()

    for j in range(1, 4):
        nums.append(j)
        is_bad_num = False
        for i in range(1, len(nums) // 2 + 1):
            if is_bad_nums(nums, i):
                is_bad_num = True

        if not is_bad_num:
            solve(nums)
        nums.pop()


solve([])
