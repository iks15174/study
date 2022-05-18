from collections import deque
import math

n, k = map(int, input().split())
max_pos = 100000


def solve():
    global n, k, max_pos
    ans = math.inf
    q = deque([])
    q.append((n, 0))
    time = [math.inf] * (max_pos + 1)
    while q:
        pos, t = q.popleft()
        if pos == k:
            return t
        if pos * 2 <= max_pos + 1 and time[pos * 2] > t:
            time[pos * 2] = t
            q.appendleft((2 * pos, t))
        if pos + 1 <= max_pos and time[pos + 1] > t + 1:
            time[pos + 1] = t + 1
            q.append((pos + 1, t + 1))
        if pos - 1 >= 0 and time[pos - 1] > t + 1:
            time[pos - 1] = t + 1
            q.append((pos - 1, t + 1))
    return ans


print(solve())
