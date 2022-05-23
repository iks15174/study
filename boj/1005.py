import sys
import heapq

input = sys.stdin.readline
t = int(input().strip())
for _ in range(t):
    n, k = map(int, input().strip().split())
    times = list(map(int, input().strip().split()))
    updated_times = [0] * n
    back_nums = [0] * n
    graph = [[] for _ in range(n)]
    for _ in range(k):
        start, end = map(int, input().strip().split())
        start = start - 1
        end = end - 1
        graph[start].append(end)
        back_nums[end] += 1
    win_building = int(input().strip())
    q = []
    for idx, b in enumerate(back_nums):
        if b == 0:
            q.append(idx)
            updated_times[idx] = times[idx]
    cur_time = 0
    while q:
        node = q.pop()
        for next_node in graph[node]:
            update_time = times[next_node] + updated_times[node]
            if update_time > updated_times[next_node]:
                updated_times[next_node] = update_time
            back_nums[next_node] -= 1
            if back_nums[next_node] == 0:
                q.append(next_node)
    print(updated_times[win_building - 1])
