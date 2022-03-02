import heapq
import sys

input = sys.stdin.readline

t = int(input())  # test case
for _ in range(t):
    op_num = int(input())
    min_heap = []
    max_heap = []
    num_appear = {}  # 각 숫자의 살아있는 수를 관리하는 딕션너리이다.
    for _ in range(op_num):
        op, num = input().strip().split()
        num = int(num)
        if op == "I":
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            if num in num_appear:  # 이미 존재하면 +1 해주고 아니면 1로 초기화 해준다.
                num_appear[num] += 1
            else:
                num_appear[num] = 1
        if op == "D":
            if num == -1:
                while len(min_heap) > 0:
                    min_value = min_heap[0]
                    if num_appear[min_value] > 0:
                        heapq.heappop(min_heap)
                        num_appear[min_value] -= 1
                        break
                    heapq.heappop(min_heap)
            elif num == 1:
                while len(max_heap) > 0:
                    max_value = -max_heap[0]
                    if num_appear[max_value] > 0:
                        heapq.heappop(max_heap)
                        num_appear[max_value] -= 1
                        break
                    heapq.heappop(max_heap)

    # 최솟값 & 최댓값 출력
    min_result = None
    max_result = None
    while len(min_heap) > 0:
        min_value = min_heap[0]
        if num_appear[min_value] > 0:
            min_result = min_value
            break
        heapq.heappop(min_heap)

    while len(max_heap) > 0:
        max_value = -max_heap[0]
        if num_appear[max_value] > 0:
            max_result = max_value
            break
        heapq.heappop(max_heap)
    if not max_result and not min_result:
        print("EMPTY")
    else:
        print(max_result, min_result)
