import math

n = int(input())
liquid = list(map(int, input().split()))
liquid = sorted(liquid)
start = 0
end = n - 1
prev_diff = math.inf
prev_op = -2  # 0이면 end - 1, 1이면 start + 1


def solve():
    global liquid, start, end, prev_diff, prev_op
    ans1 = -1
    ans2 = -1

    while start < end:
        diff = liquid[start] + liquid[end]
        if diff == 0:
            print(liquid[start], liquid[end])
            return
        if abs(diff) < prev_diff:
            ans1 = start
            ans2 = end
            prev_diff = abs(diff)

        if diff < 0:
            start += 1
        else:
            end -= 1

    print(liquid[ans1], liquid[ans2])


solve()
