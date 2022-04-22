from collections import deque

sdoku = []
row_num = [[0] * 9 for _ in range(9)]  # 각 row 나타난 숫자의 갯수
col_num = [[0] * 9 for _ in range(9)]  # 각 column 나타난 숫자의 갯수
square_num = [[0] * 9 for _ in range(9)]  # 각 square 나타난 숫자의 갯수
zero_pos = deque()
finished = False


def square(row, col):
    return ((row // 3) * 3) + col // 3


def print_sdoku(sdoku):
    for line in sdoku:
        print("".join(map(str, line)))


for _ in range(9):
    sdoku.append(list(map(int, list(str(input())))))

for row in range(9):
    for col in range(9):
        if sdoku[row][col] == 0:
            zero_pos.append((row, col))
        else:
            row_num[row][sdoku[row][col] - 1] = 1
            col_num[col][sdoku[row][col] - 1] = 1
            square_num[square(row, col)][sdoku[row][col] - 1] = 1


def solve():
    global sdoku, row_num, col_num, square_num, zero_pos, finished
    if len(zero_pos) == 0:
        print_sdoku(sdoku)
        finished = True
        exit()
    pos = zero_pos.popleft()
    for num in range(9):
        if (
            row_num[pos[0]][num] == 0
            and col_num[pos[1]][num] == 0
            and square_num[square(pos[0], pos[1])][num] == 0
        ):
            row_num[pos[0]][num] = 1
            col_num[pos[1]][num] = 1
            square_num[square(pos[0], pos[1])][num] = 1
            sdoku[pos[0]][pos[1]] = num + 1
            solve()
            row_num[pos[0]][num] = 0
            col_num[pos[1]][num] = 0
            square_num[square(pos[0], pos[1])][num] = 0
            sdoku[pos[0]][pos[1]] = 0

    zero_pos.appendleft(pos)


solve()
