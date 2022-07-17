def solution(n, cores):
    left = 0
    right = 50000 * 10000
    while left < right:
        mid = (left + right) // 2
        task = 0
        for c in cores:
            task += (mid // c) + 1
        if task >= n:
            right = mid
        else:
            left = mid + 1
    answer = 0
    lack_num = 0
    prev_total = 0
    for c in cores:
        prev_total += (right - 1) // c + 1
    lack_num = n - prev_total
    for idx, c in enumerate(cores):
        if right % c == 0:
            lack_num -= 1
            if lack_num == 0:
                return idx + 1