import math
import sys

input = sys.stdin.readline
n, m, b = map(int, input().strip().split())
board = [list(map(int, input().strip().split())) for _ in range(n)]
flat_b = sorted(sum(board, []), reverse=True)
max_len = max(flat_b)

ans_time = math.inf
ans_h = 0
for h in range(max_len + 1):
    temp_b = b
    time = 0
    for block in flat_b:
        if block > h:
            temp_b += (block - h)
            time += 2 * (block - h)
        elif block < h:
            if temp_b >= (h - block):
                temp_b -= (h - block)
                time += (h - block)
            else:
                time = math.inf
                break
    if time <= ans_time:
        ans_time = time
        ans_h = max(ans_h, h)

print(ans_time, ans_h)    
