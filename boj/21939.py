import heapq
import sys

input = sys.stdin.readline

problem_dic = {}
min_heapq = []
max_heapq = []
n = int(input().strip())
for _ in range(n):
    problem, level = map(int, input().strip().split())
    heapq.heappush(min_heapq, (level, problem))
    heapq.heappush(max_heapq, (-level, -problem))
    problem_dic[problem] = level

m = int(input().strip())
for _ in range(m):
    cmd_list = list(input().strip().split())
    cmd = cmd_list[0]
    nums = list(map(int, cmd_list[1:]))
    if cmd == "recommend":
        if nums[0] == 1:
            while True:
                if problem_dic[-max_heapq[0][1]] == -max_heapq[0][0]:
                    print(-max_heapq[0][1])
                    break
                else:
                    heapq.heappop(max_heapq)
        else:
            while True:
                if problem_dic[min_heapq[0][1]] == min_heapq[0][0]:
                    print(min_heapq[0][1])
                    break
                else:
                    heapq.heappop(min_heapq)

    elif cmd == "add":
        heapq.heappush(max_heapq, (-nums[1], -nums[0]))
        heapq.heappush(min_heapq, (nums[1], nums[0]))
        problem_dic[nums[0]] = nums[1]
    else:
        problem_dic[nums[0]] = -1
