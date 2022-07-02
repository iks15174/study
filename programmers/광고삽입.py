def time_to_num(time):
    h, m, s = map(int, time.split(':'))
    return h * 60 * 60 + m * 60 + s

def num_to_time(num):
    h = num // 3600
    m = (num % 3600) // 60
    s = num % 60
    h = '0' + str(h) if h < 10 else str(h)
    m = '0' + str(m) if m < 10 else str(m)
    s = '0' + str(s) if s < 10 else str(s)
    return h + ':' + m + ':' + s
    
def solution(play_time, adv_time, logs):
    play_time = time_to_num(play_time)
    adv_time = time_to_num(adv_time)
    time_sum = [0] * (play_time + 1)
    for l in logs:
        stime, etime = l.split('-')
        stime = time_to_num(stime)
        etime = time_to_num(etime)
        time_sum[stime] += 1
        time_sum[etime] -= 1
    for i in range(len(time_sum) - 1):
        time_sum[i + 1] += time_sum[i]
    start = 0
    max_value = 0
    for i in range(adv_time):
        max_value += time_sum[i]
    prev_value = max_value
    for i in range(play_time - adv_time + 1):
        cur_value = prev_value - time_sum[i] + time_sum[i + adv_time]
        if cur_value > max_value:
            max_value = cur_value
            start = i + 1
        prev_value = cur_value
    return num_to_time(start)