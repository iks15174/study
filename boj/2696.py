import sys
import heapq

input = sys.stdin.readline
t = int(input().strip())

for _ in range(t):
    m = int(input().strip())
    queue = []
    result_q = []
    bigger_queue = []
    smaller_queue = (
        []
    )  # smaller queue의 모든 값은 bigger queue의 모든 값보다 작다. smaller queue의 가장 큰 값이 중앙값이다.

    # 입력을 받는다.
    while m > 0:
        input_line = list(map(int, input().strip().split()))
        for num in input_line:
            queue.append(num)
        m -= 10

    for idx, num in enumerate(queue):
        if idx % 2 == 0:
            heapq.heappush(smaller_queue, -num)  # max heap을 의미한다.
        if idx % 2 == 1:
            heapq.heappush(bigger_queue, num)  # min heap을 의미한다.

        if len(bigger_queue) > 0 and -smaller_queue[0] > bigger_queue[0]:
            big_value = -heapq.heappop(smaller_queue)
            small_value = heapq.heappop(bigger_queue)
            heapq.heappush(bigger_queue, big_value)
            heapq.heappush(smaller_queue, -small_value)

        if idx % 2 == 0:
            result_q.append(-smaller_queue[0])

    line_formatted = []
    print(len(result_q))
    for idx, result_n in enumerate(result_q):
        line_formatted.append(result_n)

        if idx % 9 == 0 and idx > 0:
            print(*line_formatted)
            line_formatted = []

    if len(line_formatted) > 0:
        print(*line_formatted)
