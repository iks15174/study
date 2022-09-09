import copy
d = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
board = [[0] * 4 for _ in range(4)]
fish_pos = [[] for _ in range(17)]
ans = -1
for r in range(4):
    info = list(map(int, input().split()))
    for c in range(4):
        board[r][c] = info[c * 2]
        fish_pos[info[c * 2]] = [r, c, info[c * 2 + 1] - 1]
  
def is_movable(cr, cc, direction):
    global d, board
    nr = cr + d[direction][0]
    nc = cc + d[direction][1]
    if nr < 0 or nr >= 4 or nc < 0 or nc >= 4 or board[nr][nc] == 17: # 17은 상어가 있는 칸이다.
        return False
    return True

def move_fish():
    global d, board, fish_pos
    for f in range(1, 17):
        if fish_pos[f][2] == -1: #사라진 물고기
            continue
        for i in range(8):
            cur_d = (fish_pos[f][2] + i) % 8
            if is_movable(fish_pos[f][0], fish_pos[f][1], cur_d):
                next_r = fish_pos[f][0] + d[cur_d][0]
                next_c = fish_pos[f][1] + d[cur_d][1]
                nf = board[next_r][next_c]
                if nf != -1: # 빈칸이 아닐 경우
                    fish_pos[nf][0] = fish_pos[f][0]
                    fish_pos[nf][1] = fish_pos[f][1]
                board[fish_pos[f][0]][fish_pos[f][1]] = nf
                fish_pos[f][0] = next_r
                fish_pos[f][1] = next_c
                fish_pos[f][2] = cur_d
                board[next_r][next_c] = f
                break
                    
                
def init(): # 상어가 (0, 0)에 들어가 먹이를 먹는다.
    global board, fish_pos
    fish_num = board[0][0]
    direct = fish_pos[fish_num][2]
    fish_pos[fish_num][2] = -1
    board[0][0] = 17
    return [direct, fish_num]


def shark_feed_candidate(shark_pos): #상어의 먹이 후보를 return 한다.
    global board, d
    cr = shark_pos[0]
    cc = shark_pos[1]
    candidate = []
    while 0 <= cr < 4 and 0 <= cc < 4:
        if 1 <= board[cr][cc] <= 16:
            candidate.append([cr, cc])
        cr += d[shark_pos[2]][0]
        cc += d[shark_pos[2]][1]
    return candidate
 
 
def solve(shark_pos, cnt):
    global board, d, fish_pos, ans
    before_move = copy.deepcopy(board)
    before_fish_pos = copy.deepcopy(fish_pos)
    move_fish()
    sfc = shark_feed_candidate(shark_pos)
    if len(sfc) == 0:
        ans = max(ans, cnt)
        board = before_move
        fish_pos = before_fish_pos
        return
    for cr, cc in sfc:
         origin_fish = board[cr][cc]
         origin_fish_dir = fish_pos[origin_fish][2]
         board[cr][cc] = 17
         fish_pos[origin_fish][2] = -1
         board[shark_pos[0]][shark_pos[1]] = -1
         solve([cr, cc, origin_fish_dir], cnt + origin_fish)
         board[cr][cc] = origin_fish
         fish_pos[origin_fish][2] = origin_fish_dir
         board[shark_pos[0]][shark_pos[1]] = 17
    board = before_move
    fish_pos = before_fish_pos
    
         
init_dir, init_cnt = init()
solve([0, 0, init_dir], init_cnt)
print(ans)