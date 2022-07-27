import heapq
def solution(n, works):
    hn = []
    for w in works:
        heapq.heappush(hn, -w)
    while n > 0:
        max_val = -heapq.heappop(hn)
        max_val = max_val - 1 if max_val > 0 else 0
        n -= 1
        heapq.heappush(hn, -max_val)
    answer = 0
    for h in hn:
        answer += h ** 2
    return answer