import heapq
from collections import OrderedDict
n = int(input())
hw = [list(map(int, input().split())) for _ in range(n)]
days = {}
for d, s in hw:
    if d not in days:
        days[d] = [s]
    else:
        days[d].append(s)
for key, item in days.items():
    days[key] = sorted(item, reverse=True)
days = OrderedDict(sorted(days.items()))
hq = []
for k, i in days.items():
    for idx, score in enumerate(i):
        if len(hq) < k:
            heapq.heappush(hq, (score, k))
        else:
            if hq[0][0] < score:
                heapq.heappop(hq)
                heapq.heappush(hq, (score, k))
            else:
                break
ans = 0
for s, k in hq:
    ans += s
print(ans)