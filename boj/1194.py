from collections import deque

r, c = map(int, input().split())
state_num = 64
visited = [[[False] * c for _ in range(r)] for _ in range(state_num)]
board = [list(input()) for _ in range(r)]


def get_init_pos():
    global r, c, board
    for i in range(r):
        for j in range(c):
            if board[i][j] == "0":
                return [i, j]


def alphabet_to_bit(alpha):
    anum = ord(alpha.lower()) - 97
    return 1 << anum


def bfs(cur_pos):
    global r, c, board, visited
    q = deque([[cur_pos, 0, 0]])  # 현재위치, 열쇠 상태, 거리
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while q:
        pos, state, dist = q.popleft()
        for m in move:
            nr = pos[0] + m[0]
            nc = pos[1] + m[1]
            if nr < 0 or nr >= r or nc < 0 or nc >= c or board[nr][nc] == "#":
                continue
            if (board[nr][nc] == "." or board[nr][nc] == '0') and not visited[state][nr][nc]:
                visited[state][nr][nc] = True
                q.append([[nr, nc], state, dist + 1])
            elif board[nr][nc].islower():
                new_state = state | alphabet_to_bit(board[nr][nc])
                if not visited[new_state][nr][nc]:
                    visited[new_state][nr][nc] = True
                    q.append([[nr, nc], new_state, dist + 1])
            elif board[nr][nc].isupper():
                if (
                    state & alphabet_to_bit(board[nr][nc])
                    and not visited[state][nr][nc]
                ):
                    visited[state][nr][nc] = True
                    q.append([[nr, nc], state, dist + 1])
            elif board[nr][nc] == '1':
                return dist + 1

    return -1


cur_pos = get_init_pos()
print(bfs(cur_pos))
