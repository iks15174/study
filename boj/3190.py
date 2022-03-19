from collections import deque

n = int(input())
board = [[0] * n for _ in range(n)]  # 보드이다. 사과는 1 이다.
board[0][0] = 2
apple_len = int(input())
snake_move = {}  # 시간, 방향의 쌍을 담고 있다.
snake_body = deque()
snake_body.append((0, 0))  # 뱀의 머리 ~ 꼬리를 의미한다.
cur_direction = (0, 1)  # 오른쪽 방향, 뱀의 진행 방향
left_rotate = [(0, 1), (-1, 0), (0, -1), (1, 0)]
right_rotate = [(0, 1), (1, 0), (0, -1), (-1, 0)]
cur_time = 0
for _ in range(apple_len):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 1
move_len = int(input())
for _ in range(move_len):
    time, direction = input().split()
    time = int(time)
    snake_move[time] = direction


def move_snake():
    head_pos = snake_body[0]
    next_row = head_pos[0] + cur_direction[0]
    next_col = head_pos[1] + cur_direction[1]
    if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n:  # 뱀이 벽이랑 부딪힐 경우
        return True
    for body_pos in snake_body:
        if body_pos[0] == next_row and body_pos[1] == next_col:
            return True

    if board[next_row][next_col] == 1:  # 사과를 먹었다.
        board[next_row][next_col] = 0
        snake_body.appendleft((next_row, next_col))
    else:
        snake_body.appendleft((next_row, next_col))
        snake_body.pop()
    return False


while True:
    cur_time += 1
    finished = move_snake()  # 뱀의 머리만 움직인다.
    if finished:
        break
    if cur_time in snake_move:
        move = snake_move[cur_time]
        if move == "L":
            index = left_rotate.index(cur_direction)
            index += 1
            cur_direction = left_rotate[index % 4]
        elif move == "D":
            index = right_rotate.index(cur_direction)
            index += 1
            cur_direction = right_rotate[index % 4]

print(cur_time)
