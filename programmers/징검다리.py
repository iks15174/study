def solution(distance, rocks, n):
    rocks = sorted(rocks)
    ds = []
    prev = 0
    for r in rocks:
        ds.append(r - prev)
        prev = r
    ds.append(distance - prev)
    left = 0
    right = distance
    ans = -1
    while left <= right:
        temp_n = n + 1
        mid = (left + right) // 2
        sum_arr = []
        sum_val = 0
        for d in ds:
            if sum_val >= mid or temp_n == 0:
                sum_arr.append(sum_val)
                sum_val = d
            else:
                sum_val += d
                temp_n -= 1
        sum_arr.append(sum_val)
        min_sum = min(sum_arr)
        if min_sum > mid:
            left = mid + 1
        elif min_sum < mid:
            right = mid - 1
        else:
            ans = max(ans, mid)
            left = mid + 1
    return ans