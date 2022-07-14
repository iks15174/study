import math
def solution(n, stations, w):
    cur_pos = 1
    station_range = 2 * w + 1
    answer = 0
    for s in stations:
        if s - w > cur_pos:
            empty = s - w - cur_pos
            answer += math.ceil(empty / station_range)
        cur_pos = s + w + 1
    if cur_pos <= n:
        empty = n - cur_pos + 1
        answer += math.ceil(empty / station_range)
    return answer
        