def find_shape(table, r, c, shape_id, val):
    q = [(r, c)]
    table[r][c] = shape_id
    n = len(table)
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    r1 = r
    c1 = c
    r2 = r
    c2 = c
    while q:
        cr, cc = q.pop()
        for m in move:
            nr = cr + m[0]
            nc = cc + m[1]
            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue
            if table[nr][nc] == val:
                table[nr][nc] = shape_id
                r1 = min(r1, nr)
                c1 = min(c1, nc)
                r2 = max(r2, nr)
                c2 = max(c2, nc)
                q.append((nr, nc))
    shape = [[0] * (c2 - c1 + 1) for _ in range(r2 - r1 + 1)]
    for sr in range(r1, r2 + 1):
        for sc in range(c1, c2 + 1):
            if table[sr][sc] == shape_id:
                shape[sr - r1][sc - c1] = 1
    return shape
            
def rotate(shape):
    rl = len(shape)
    cl = len(shape[0])
    rotated_shape = [[0] * rl for _ in range(cl)]
    for r in range(rl):
        for c in range(cl):
            rotated_shape[cl - c - 1][r] = shape[r][c]
    return rotated_shape

def solution(game_board, table):
    n = len(game_board)
    shape_id = 2
    shapes = []
    shapes_board = []
    for r in range(n):
        for c in range(n):
            if table[r][c] == 1:
                shapes.append(find_shape(table, r, c, shape_id, 1))
                shape_id += 1
    
    shape_id = 2
    for r in range(n):
        for c in range(n):
            if game_board[r][c] == 0:
                shapes_board.append(find_shape(game_board, r, c, shape_id, 0))
                shape_id += 1
            
    used_idx = [False] * len(shapes)
    answer = 0
    for sb in shapes_board:
        found = False
        for idx, s in enumerate(shapes):
            if found:
                break
            if used_idx[idx]:
                continue
            for _ in range(4):
                s = rotate(s)
                if s == sb:
                    used_idx[idx] = True
                    answer += sum([sum(i) for i in s])
                    found = True
                    break
    return answer
