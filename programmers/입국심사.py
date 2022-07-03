def solve(min, max, times, n):
    left = min
    right = max
    while left < right:
        mid = (left + right) // 2
        exam_num = 0
        for t in times:
            exam_num += mid // t
        if exam_num < n:
            left = mid + 1
        else:
            right = mid
    return right
        
def solution(n, times):
    answer = 0
    max_time = (n // len(times) + 1) * max(times)
    answer = solve(0, max_time, times, n)
    return answer