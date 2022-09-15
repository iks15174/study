import sys
import math

input = sys.stdin.readline
n, m = map(int, input().split())
rides = list(map(int, input().split()))
if n <= m:
    print(n)
    sys.exit()
max_time = (n // m + 1) * max(rides)
left = 1
right = max_time
while left < right:
    mid = (left + right) // 2
    complete = 0
    for r in rides:
        complete += math.floor(mid / r + 1)
    if complete < n:
        left = mid + 1
    else:
        right = mid
ans = 0
before_people = 0
for r in rides:
    before_people += math.floor((right - 1) / r + 1)
left_people = n - before_people
for idx, r in enumerate(rides):
    if right % r == 0:
        left_people -= 1
        if left_people == 0:
            ans = idx + 1
            break
print(ans)