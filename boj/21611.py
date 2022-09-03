from collections import deque
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
explode_cnt = [0, 0, 0]
def magic(d, s):
    global board, n
    direc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    cur_d = direc[d - 1]
    cr, cc = (n - 1) // 2, (n - 1) // 2
    for _ in range(s):
        cr += cur_d[0]
        cc += cur_d[1]
        if cr < 0 or cr >= n or cc < 0 or cc >= n:
            break
        board[cr][cc] = 0
        
def move_ball():
    global board, n
    direction = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    cur_d = 1
    m_cnt = 1
    cur_m_cnt = 1
    cr, cc = (n - 1) // 2, (n - 1) // 2 - 1
    empty_space = deque([])
    while 0 <= cr < n and 0 <= cc < n:
        if board[cr][cc] == 0:
            empty_space.append([cr, cc])
        else:
            if empty_space:
                er, ec = empty_space.popleft()
                board[er][ec] = board[cr][cc]
                board[cr][cc] = 0
                empty_space.append([cr, cc])
        cr += direction[cur_d][0]
        cc += direction[cur_d][1]
        m_cnt -= 1
        if m_cnt == 0:
            cur_d = (cur_d + 1) % 4
            if cur_d == 2 or cur_d == 0:
                cur_m_cnt += 1
            m_cnt = cur_m_cnt
        
def explode():
    global board, n, explode_cnt
    is_exploded = False
    direction = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    cur_d = 1
    m_cnt = 1
    cur_m_cnt = 1
    cr, cc = (n - 1) // 2, (n - 1) // 2 - 1
    same_pos = []
    prev_val = 0
    same_cnt = 1
    while 0 <= cr < n and 0 <= cc < n:
        if board[cr][cc] == prev_val:
            same_cnt += 1
            same_pos.append([cr, cc])
        else:
            if same_cnt >= 4:
                is_exploded = True
                explode_cnt[prev_val - 1] += same_cnt
                for sr, sc in same_pos:
                    board[sr][sc] = 0
            same_cnt = 1
            prev_val = board[cr][cc]
            same_pos = [[cr, cc]]
        cr += direction[cur_d][0]
        cc += direction[cur_d][1]
        m_cnt -= 1
        if m_cnt == 0:
            cur_d = (cur_d + 1) % 4
            if cur_d == 2 or cur_d == 0:
                cur_m_cnt += 1
            m_cnt = cur_m_cnt
    return is_exploded
            
def change():
    global board, n
    direction = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    new_board = [[0] * n for _ in range(n)]
    result = []
    cur_d = 1
    m_cnt = 1
    cur_m_cnt = 1
    cr, cc = (n - 1) // 2, (n - 1) // 2 - 1
    prev_val = 0
    same_cnt = 1
    while 0 <= cr < n and 0 <= cc < n:
        if board[cr][cc] == prev_val:
            same_cnt += 1
        else:
            if prev_val != 0:
                result.append(same_cnt)
                result.append(prev_val)
            same_cnt = 1
            prev_val = board[cr][cc]
            if len(result) >= (n ** 2 - 1):
                break
        cr += direction[cur_d][0]
        cc += direction[cur_d][1]
        m_cnt -= 1
        if m_cnt == 0:
            cur_d = (cur_d + 1) % 4
            if cur_d == 2 or cur_d == 0:
                cur_m_cnt += 1
            m_cnt = cur_m_cnt
    
    cur_d = 1
    m_cnt = 1
    cur_m_cnt = 1
    cr, cc = (n - 1) // 2, (n - 1) // 2 - 1
    for r in result:
        new_board[cr][cc] = r
        cr += direction[cur_d][0]
        cc += direction[cur_d][1]
        m_cnt -= 1
        if m_cnt == 0:
            cur_d = (cur_d + 1) % 4
            if cur_d == 2 or cur_d == 0:
                cur_m_cnt += 1
            m_cnt = cur_m_cnt
    board = new_board      
                   
    
        
        
for _ in range(m):
    d, s = map(int, input().split())
    magic(d, s)
    move_ball()
    while explode():
        move_ball()
    change()
ans = 0
for idx, ex in enumerate(explode_cnt):
    ans += (idx + 1) * ex
print(ans)