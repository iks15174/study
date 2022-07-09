import math
from collections import deque
def solution(board):
    answer = math.inf
    b_len = len(board)
    visited = [[[math.inf, math.inf] for _ in range(b_len)] for _ in range(b_len)]
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    q = deque([[0, 0, 0, 0], [0, 0, 1, 0]]) # x, y, 방향, 비용을 의미한다. 0은 상하, 1은 좌우를 의미한다.
    visited[0][0][0] = 0
    visited[0][0][1] = 0
    while q:
        cr, cc, cdir, cost = q.popleft()
        # print(cr, cc, cdir, cost)
        for idx, m in enumerate(move):
            nr = cr + m[0]
            nc = cc + m[1]
            ndir = idx // 2
            ncost = cost + (100 if cdir == ndir else 600)
            if nr < 0 or nr >= b_len or nc < 0 or nc >= b_len:
                continue
            if nr == b_len - 1 and nc == b_len - 1:
                answer = min(answer, ncost)
                continue
            if visited[nr][nc][ndir] > ncost and board[nr][nc] == 0:
                visited[nr][nc][ndir] = ncost
                q.append([nr, nc, ndir, ncost])
            
    return answer