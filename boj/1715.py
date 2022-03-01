# 가장 작은 카드 뭉치부터 차례로 더해간다.
import heapq

n = int(input())
queue = []
for _ in range(n):
    card = int(input())
    heapq.heappush(queue, card)

result = 0
for _ in range(n - 1):
    card1 = heapq.heappop(queue)
    card2 = heapq.heappop(queue)
    twoCards = card1 + card2
    result += twoCards
    heapq.heappush(queue, twoCards)

print(result)
