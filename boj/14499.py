# dice 배열은 주사위의 위치를 의미한다.
# dice가 나타내는 주사위는 (index의미)2가 바닥, 3이 동쪽, 0이 북쪽을 바라본다.
# 주사위가 구를 때 마다 dice를 업데이트 해줘야 한다.
import copy

# 입력을 받는다.
n, m, x, y, op_len = map(int, input().split())
board = [[] for _ in range(n)]
dice = [0] * 6
for i in range(n):
    line = list(map(int, input().split()))
    board[i] = line
operation = list(map(int, input().split()))

# 주사위의 움직임 정의
def move_dice(op):
    temp = copy.deepcopy(dice)
    if op == 1:
        dice[2] = temp[3]
        dice[1] = temp[2]
        dice[5] = temp[1]
        dice[3] = temp[5]
    elif op == 2:
        dice[2] = temp[1]
        dice[3] = temp[2]
        dice[1] = temp[5]
        dice[5] = temp[3]
    elif op == 3:
        dice[2] = temp[4]
        dice[4] = temp[5]
        dice[5] = temp[0]
        dice[0] = temp[2]
    elif op == 4:
        dice[2] = temp[0]
        dice[4] = temp[2]
        dice[5] = temp[4]
        dice[0] = temp[5]


# 동서남북의 움직임 정의
move = [[0, 1], [0, -1], [-1, 0], [1, 0]]

# 명령어를 실행한다.
for op in operation:
    next_x = x + move[int(op) - 1][0]
    next_y = y + move[int(op) - 1][1]

    # 범위를 벗어났는지 확인
    if next_x >= 0 and next_x < n and next_y >= 0 and next_y < m:
        x = next_x
        y = next_y
    else:
        continue

    move_dice(op)
    if board[x][y] == 0:
        board[x][y] = dice[2]
    else:
        dice[2] = board[x][y]
        board[x][y] = 0

    print(dice[5])
