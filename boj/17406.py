from copy import deepcopy
from itertools import permutations
import math

n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
rotation_op = [list(map(int, input().split())) for _ in range(k)]


def array_value(board):
    min_val = math.inf
    for row in board:
        min_val = min(min_val, sum(row))
    return min_val


def rotate(s_r, s_c, f_r, f_c, board):  # 각각 start_row,col / finish_row, col 을 의미한다.
    tmp = board[s_r][s_c]
    for i in range(s_r, f_r):  # 왼쪽 부분 변경
        board[i][s_c] = board[i + 1][s_c]

    for i in range(s_c, f_c):  # 아래 부분 변경
        board[f_r][i] = board[f_r][i + 1]

    for i in range(f_r, s_r, -1):  # 오른쪽 부분 변경
        board[i][f_c] = board[i - 1][f_c]

    for i in range(f_c, s_c + 1, -1):  # 위 부분 변경
        board[s_r][i] = board[s_r][i - 1]

    board[s_r][s_c + 1] = tmp


def rotate_board(r, c, s, board):
    s_r = r - s
    s_c = c - s
    f_r = r + s
    f_c = c + s
    for _ in range(s):  # 가운데 1개 정사각형이 되기 전까지
        rotate(s_r, s_c, f_r, f_c, board)
        s_r += 1
        s_c += 1
        f_r -= 1
        f_c -= 1


ans = math.inf
for per_op in permutations(rotation_op, k):
    copy_board = [r[:] for r in board]
    for op in per_op:
        rotate_board(op[0] - 1, op[1] - 1, op[2], copy_board)
        ans = min(ans, array_value(copy_board))
    # print("----------")
    # for b in copy_board:
    #     print(b)

print(ans)
