from collections import deque
def time_to_num(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m

def solution(n, t, m, timetable):
    start_t = time_to_num("09:00")
    last_t = (n - 1) * t + start_t
    timetable_n = []
    for tb in timetable:
        timetable_n.append(time_to_num(tb))
    timetable_n = deque(sorted(timetable_n))
    for i in range(n - 1):
        cur_time = start_t + i * t
        cnt = 0
        while cnt < m and len(timetable_n) > 0:
            if timetable_n[0] <= cur_time:
                timetable_n.popleft()
            cnt += 1
            
    cur_time = start_t + (n - 1) * t
    while len(timetable_n) > 0:
        if timetable_n[-1] > cur_time:
            timetable_n.pop()
        else:
            break
    
    answer = 0
    if len(timetable_n) < m:
        answer = last_t
    else:
        answer = timetable_n[m - 1] - 1
    return str(answer // 60).zfill(2) + ":" + str(answer % 60).zfill(2)

# 두번쨰 풀이
import bisect

def time_to_num(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m

def solution(n, t, m, timetable):
    timetable_int = sorted([time_to_num(t) for t in timetable])
    takeon_info = {}
    start = time_to_num('09:00')
    for i in range(n):
        takeon_info[start + i * t] = []
    for ti in timetable_int:
        for taketime in takeon_info.keys():
            if ti <= taketime and len(takeon_info[taketime]) < m:
                takeon_info[taketime].append(ti)
                break
                
    for pt in range(time_to_num('24:00')):
        found = False
        for k, v in takeon_info.items():
            if k < pt:
                continue
            possible_idx = bisect.bisect_right(v, pt)
            if possible_idx < m:
                found = True
                break
        if not found:
            return str((pt - 1) // 60).zfill(2) + ":" + str((pt - 1) % 60).zfill(2) 
        
    