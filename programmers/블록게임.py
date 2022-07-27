possible_block = [
    [[1, 0, 0], [1, 1, 1]],
    [[0, 1], [0, 1], [1, 1]],
    [[1, 0], [1, 0], [1, 1]],
    [[0, 0, 1], [1, 1, 1]],
    [[0, 1, 0], [1, 1, 1]],
]


def check_shape(lr, lc, rr, rc, board, id):
    global possible_block
    rowl = rr - lr + 1
    coll = rc - lc + 1
    for pb in possible_block:
        if len(pb) == rowl and len(pb[0]) == coll:
            is_diff = False
            for ridx in range(rowl):
                for cidx in range(coll):
                    b_filled = True if board[lr + ridx][lc + cidx] == id else False
                    pb_filled = True if pb[ridx][cidx] > 0 else False
                    if b_filled != pb_filled:
                        is_diff = True
            if not is_diff:
                return True
    return False


def can_crash(lr, lc, rr, rc, board, block_id):
    rowl = rr - lr + 1
    coll = rc - lc + 1
    for ridx in range(rowl):
        for cidx in range(coll):
            if board[lr + ridx][lc + cidx] != 0 and board[lr + ridx][lc + cidx] != block_id:
                return False
            if board[lr + ridx][lc + cidx] == 0:
                cur_row = lr + ridx
                while cur_row >= 0:
                    if board[cur_row][lc + cidx] != 0:
                        return False
                    cur_row -= 1
    return True


def crash(lr, lc, rr, rc, board, block_id):
    rowl = rr - lr + 1
    coll = rc - lc + 1
    for ridx in range(rowl):
        for cidx in range(coll):
            if board[lr + ridx][lc + cidx] == block_id:
                board[lr + ridx][lc + cidx] = 0


def dfs(r, c, visited, board, n):
    move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    shape_id = board[r][c]
    visited[r][c] = True
    q = [[r, c]]
    lr = r
    rr = r
    lc = c
    rc = c
    while q:
        cr, cc = q.pop()
        for m in move:
            nr = cr + m[0]
            nc = cc + m[1]
            if (
                nr < 0
                or nr >= n
                or nc < 0
                or nc >= n
                or board[nr][nc] != shape_id
                or visited[nr][nc]
            ):
                continue
            q.append((nr, nc))
            visited[nr][nc] = True
            lr = min(lr, nr)
            rr = max(rr, nr)
            lc = min(lc, nc)
            rc = max(rc, nc)
    return (lr, lc, rr, rc)


def solution(board):
    n = len(board)
    visited = [[False] * n for _ in range(n)]
    candidate = []
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0 and not visited[i][j]:
                lr, lc, rr, rc = dfs(i, j, visited, board, n)
                if check_shape(lr, lc, rr, rc, board, board[i][j]):
                    candidate.append((lr, lc, rr, rc, board[i][j]))
    answer = 0
    while True:
        prev_answer = answer
        candidate_temp = []
        for c in candidate:
            if can_crash(c[0], c[1], c[2], c[3], board, c[4]):
                crash(c[0], c[1], c[2], c[3], board, c[4])
                answer += 1
            else:
                candidate_temp.append(c)
        candidate = candidate_temp
        if prev_answer == answer:
            break
    return answer