import copy
from collections import deque
import math
from itertools import permutations

board = [[] for _ in range(5)]
move = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
for i in range(25):
    board[i // 5].append(list(map(int, input().split())))


def rotate(num):  # num번째 판을 회전시키겠다.
    origin = copy.deepcopy(board[num])
    for i in range(5):
        for j in range(5):
            board[num][i][j] = origin[4 - j][i]


def search_maze(new_board):
    global move
    if new_board[0][0][0] == 0:
        return -1
    q = deque([[0, 0, 0, 0]])
    visited = [[[False] * 5 for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = True
    while q:
        x, y, z, cost = q.popleft()
        for m in move:
            nx = x + m[0]
            ny = y + m[1]
            nz = z + m[2]
            if (
                nx < 0
                or nx >= 5
                or ny < 0
                or ny >= 5
                or nz < 0
                or nz >= 5
                or new_board[nx][ny][nz] == 0
            ):
                continue
            if visited[nx][ny][nz]:
                continue
            if nx == 4 and ny == 4 and nz == 4:
                return cost + 1
            q.append([nx, ny, nz, cost + 1])
            visited[nx][ny][nz] = True
    return -1


ans = math.inf


def solve(depth):
    global ans, board, cnt
    if depth == 5:
        for new_board in permutations(
            [board[0], board[1], board[2], board[3], board[4]], 5
        ):
            temp_ans = search_maze(new_board)
            if temp_ans != -1:
                ans = min(ans, temp_ans)
        return
    for _ in range(4):
        solve(depth + 1)
        rotate(depth)


solve(0)
print(ans if ans != math.inf else -1)
