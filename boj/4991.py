from collections import deque
import math
from os import stat

while True:
    col, row = map(int, input().split())
    if row == 0 and col == 0:
        break
    board = [list(input()) for _ in range(row)]
    start = []
    dirty_id = 0
    for r in range(row):
        for c in range(col):
            if board[r][c] == 'o':
                start = [r, c]
            elif board[r][c] == '*':
                board[r][c] = dirty_id
                dirty_id += 1
    
    
    visited = [[[False] * (col) for _ in range(row)] for _ in range(2 ** dirty_id)]
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    q = deque([[start, 0, 0]]) # 위치, state, dist를 의미한다.
    visited[0][start[0]][start[1]] = True
    ans = math.inf
    while q:
        cp, state, dist = q.popleft()
        # print(cp, state, dist)
        for m in move:
            cur_state = state
            nr = cp[0] + m[0]
            nc = cp[1] + m[1]
            if nr < 0 or nr >= row or nc < 0 or nc >= col or board[nr][nc] == 'x':
                continue
            # print(type(board[nr][nc]))
            if type(board[nr][nc]) == int and 0 <= board[nr][nc] < dirty_id:
                cur_state = cur_state | 1 << board[nr][nc]
            if visited[cur_state][nr][nc]:
                continue
            
            if cur_state == 2 ** dirty_id - 1:
                ans = min(ans, dist + 1)
                continue
            visited[cur_state][nr][nc] = True
            q.append([[nr, nc], cur_state, dist + 1])
    
    if ans == math.inf:
        print(-1)
    else:
        print(ans)