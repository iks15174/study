from collections import deque

row, col = map(int, input().split())
board = [list(input()) for _ in range(row)]
direction = [[1, 0], [0, -1], [-1, 0], [0, 1]]
r_pos = None
b_pos = None
visited = [
    [[[False] * col for _ in range(row)] for _ in range(col)] for _ in range(row)
]
for i in range(row):
    for j in range(col):
        if board[i][j] == "R":
            r_pos = (i, j)
            board[i][j] = "."
        if board[i][j] == "B":
            b_pos = (i, j)
            board[i][j] = "."


def is_movable(target, neigbor, dir):
    if board[target[0]][target[1]] == "O":
        return False
    if (
        board[target[0] + dir[0]][target[1] + dir[1]] == "."
        or board[target[0] + dir[0]][target[1] + dir[1]] == "O"
    ) and not (
        target[0] + dir[0] == neigbor[0]
        and target[1] + dir[1] == neigbor[1]
        and board[neigbor[0]][neigbor[1]] != "O"
    ):
        return True
    return False


def move(r, b, dir):
    global board
    cur_rr = r[0]
    cur_rc = r[1]
    cur_br = b[0]
    cur_bc = b[1]
    while is_movable((cur_rr, cur_rc), (cur_br, cur_bc), dir):
        cur_rr += dir[0]
        cur_rc += dir[1]

    while is_movable((cur_br, cur_bc), (cur_rr, cur_rc), dir):
        cur_br += dir[0]
        cur_bc += dir[1]

    while is_movable((cur_rr, cur_rc), (cur_br, cur_bc), dir):
        cur_rr += dir[0]
        cur_rc += dir[1]

    while is_movable((cur_br, cur_bc), (cur_rr, cur_rc), dir):
        cur_br += dir[0]
        cur_bc += dir[1]

    return [(cur_rr, cur_rc), (cur_br, cur_bc)]


def solve():
    global r_pos, b_pos, board, direction, visited
    q = deque([(r_pos, b_pos, 0)])  # red위치, blue위치, cost를 의미한다.
    while q:
        rp, bp, cost = q.popleft()
        if cost >= 10:
            break
        for d in direction:
            new_r_pos, new_b_pos = move(rp, bp, d)
            if board[new_b_pos[0]][new_b_pos[1]] != "O":
                if board[new_r_pos[0]][new_r_pos[1]] == "O":
                    return cost + 1
                if not visited[new_r_pos[0]][new_r_pos[1]][new_b_pos[0]][new_b_pos[1]]:
                    visited[new_r_pos[0]][new_r_pos[1]][new_b_pos[0]][
                        new_b_pos[1]
                    ] = True
                    q.append((new_r_pos, new_b_pos, cost + 1))
    return -1


print(solve())
