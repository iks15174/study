def solution(stones, k):
    left = min(stones)
    right = max(stones)
    while left < right:
        mid = (left + right) // 2
        cnt = 0
        for s in stones:
            if s - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            right = mid
        else:
            left = mid + 1
    return right