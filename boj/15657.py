n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
unique_nums = [nums[0]]
for n in nums:
    if n == unique_nums[-1]:
        continue
    unique_nums.append(n)


def solve(length, cur_idx, result):
    global unique_nums
    if length == 0:
        print(" ".join(list(map(str, result))))
        return
    for i in range(cur_idx, len(unique_nums)):
        result.append(unique_nums[i])
        solve(length - 1, i, result)
        result.pop()


solve(m, 0, [])
