def str_to_time(time):
    date, complete, duration = time.split()
    hour, minute, sec = map(float, complete.split(":"))
    duration = float(duration[:-1])
    complete = hour * 60 * 60 * 1000 + minute * 60 * 1000 + sec * 1000
    duration = duration * 1000
    start = complete - duration + 1 if complete - duration + 1 >= 0 else 0.0
    return [start, complete]

def solution(lines):
    times = []
    interval = []
    for l in lines:
        s, c = str_to_time(l)
        interval.append([s, c])
        times.append(s)
        times.append(c)
    times = sorted(times)
    
    ans = -1
    for t in times:
        temp_ans = 0
        for s, c in interval:
            ts = t
            te = t + 999
            if (ts <= s and te >= s) or (ts > s and ts <= c):
                temp_ans += 1
        ans = max(ans, temp_ans)
    return ans