from itertools import permutations
from collections import deque
import math

ans = math.inf
board_g = []
cards = dict()
move = [[1, 0], [-1, 0], [0, 1], [0, -1]] # 하 상 우 좌
def move_ctrl(cr, cc, dir):
    global board_g, move
    while True:
        cr = cr + move[dir][0]
        cc = cc + move[dir][1]
        if cr < 0 or cr >= 4 or cc < 0 or cc >= 4:
            return (cr - move[dir][0], cc - move[dir][1])
        if board_g[cr][cc] != 0:
            return (cr, cc)
        
def get_min_dist(fromr, fromc, trgtr, trgtc):
    global board_g, move
    if fromr == trgtr and fromc == trgtc:
        return 0
    q = deque([[fromr, fromc, 0]])
    visited = [[False] * 4 for _ in range(4)]
    visited[fromr][fromc] = True
    while q:
        cr, cc, dist = q.popleft()
        for idx, m in enumerate(move):
            nr = cr + m[0]
            nc = cc + m[1]
            if nr < 0 or nr >=4 or nc < 0 or nc >= 4:
                continue
            if not visited[nr][nc]:
                if nr == trgtr and nc == trgtc:
                    return dist + 1
                visited[nr][nc] = True
                q.append([nr, nc, dist + 1])
            
            nr, nc = move_ctrl(cr, cc, idx)
            if not visited[nr][nc]:
                if nr == trgtr and nc == trgtc:
                    return dist + 1
                visited[nr][nc] = True
                q.append([nr, nc, dist + 1])

def solve(keys, cr, cc, cnt):
    global board_g, cards, ans
    if len(keys) == 0:
        ans = min(ans, cnt)
        return
    cur_key = keys.popleft()
    
    move_cnt = get_min_dist(cr, cc, cards[cur_key][0][0], cards[cur_key][0][1])
    board_g[cards[cur_key][0][0]][cards[cur_key][0][1]] = 0
    move_cnt += get_min_dist(cards[cur_key][0][0], cards[cur_key][0][1], cards[cur_key][1][0], cards[cur_key][1][1])
    board_g[cards[cur_key][1][0]][cards[cur_key][1][1]] = 0
    
    solve(keys, cards[cur_key][1][0], cards[cur_key][1][1], cnt + move_cnt + 2)
    
    board_g[cards[cur_key][0][0]][cards[cur_key][0][1]] = cur_key
    board_g[cards[cur_key][1][0]][cards[cur_key][1][1]] = cur_key
    
    move_cnt = get_min_dist(cr, cc, cards[cur_key][1][0], cards[cur_key][1][1])
    board_g[cards[cur_key][1][0]][cards[cur_key][1][1]] = 0
    move_cnt += get_min_dist(cards[cur_key][1][0], cards[cur_key][1][1], cards[cur_key][0][0], cards[cur_key][0][1])
    board_g[cards[cur_key][0][0]][cards[cur_key][0][1]] = 0
    
    solve(keys, cards[cur_key][0][0], cards[cur_key][0][1], cnt + move_cnt + 2)
    
    board_g[cards[cur_key][0][0]][cards[cur_key][0][1]] = cur_key
    board_g[cards[cur_key][1][0]][cards[cur_key][1][1]] = cur_key
    keys.appendleft(cur_key)
    
def solution(board, r, c):
    global board_g, cards, ans
    board_g = board
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                if board[i][j] not in cards:
                    cards[board[i][j]] = [(i, j)]
                else:
                    cards[board[i][j]].append((i, j))
    for order_key in permutations(list(cards.keys())):
        solve(deque(order_key), r, c, 0)
    return ans

print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))