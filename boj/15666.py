n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
unique_nums = []
used = []
for n in nums:
    if not n in used:
        unique_nums.append(n)
        used.append(n)


def solve(cur_idx, depth, arr):
    global n, m, unique_nums
    if depth == m:
        print(" ".join(map(str, arr)))
        return
    for i in range(cur_idx, len(unique_nums)):
        arr.append(unique_nums[i])
        solve(i, depth + 1, arr)
        arr.pop()


solve(0, 0, [])
