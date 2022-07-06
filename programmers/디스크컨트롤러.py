import heapq
def solution(jobs):
    jobs_by_time = [[] for _ in range(1001)]
    for start, duration in jobs:
        jobs_by_time[start].append((duration, start))
    cur_time = 0
    all_time = 0
    finish_job = 0
    job_q = []
    for d in jobs_by_time[0]:
        heapq.heappush(job_q, d)
    
    while finish_job != len(jobs):
        if job_q:
            cur_d, cur_s = heapq.heappop(job_q)
            cur_time += cur_d
            all_time += (cur_time - cur_s)
            finish_job += 1
            for t in range(cur_time - cur_d + 1, min(1001, cur_time + 1)):
                for d in jobs_by_time[t]:
                    heapq.heappush(job_q, d)
        else:
            cur_time += 1
            for d in jobs_by_time[cur_time]:
                heapq.heappush(job_q, d)
    return all_time // len(jobs)