import sys
import math

sys.setrecursionlimit(100000)
input = sys.stdin.readline
r, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
dp = [[[-math.inf] * c for _ in range(r)] for _ in range(8)] #하, 좌, 우 로만 이동할 수 잇으므로
visited = [[False] * c for _ in range(r)]
visited[0][0] = True
def to_bit(cr, cc, visited):
    global r, c
    move = [[-1, 0], [0, -1], [0, 1]]
    val = 1
    bit = 0
    for m in move:
        nr = cr + m[0]
        nc = cc + m[1]
        cur_val = 0
        if nr < 0 or nr >= r or nc < 0 or nc >= c or visited[nr][nc]:
            cur_val = val
        bit += cur_val
        val *= 2
    return bit
        
def solve(cr, cc, visited):
    global board, r, c, dp
    move = [[1, 0], [0, -1], [0, 1]]
    cur_bit = to_bit(cr, cc, visited)
    if dp[cur_bit][cr][cc] != -math.inf:
        return dp[cur_bit][cr][cc]
    if cr == r - 1 and cc == c - 1:
        return board[cr][cc]
    temp = -math.inf + 1
    for m in move:
        nr = cr + m[0]
        nc = cc + m[1]
        if nr < 0 or nr >= r or nc < 0 or nc >= c or visited[nr][nc]:
            continue
        visited[nr][nc] = True
        temp = max(temp, solve(nr, nc, visited) + board[cr][cc])
        visited[nr][nc] = False
    dp[cur_bit][cr][cc] = temp
    return temp
print(solve(0, 0, visited))