import copy

n = int(input())
board = [[0] * n for _ in range(n)]
max_block = -1
for i in range(n):
    line = list(map(int, input().split()))
    board[i] = line


def move(board, direction):  # direction 0, 1, 2, 3은 각각 상,하,좌,우 를 의미한다.
    global n
    board_merged = [[False] * n for _ in range(n)]  # 각 칸의 숫자가 합쳐졌는지 여부를 의미한다.
    if direction == 0:
        for row in range(1, n):
            for col in range(n):
                next_row = row - 1
                while next_row >= 0 and board[next_row][col] == 0:
                    next_row -= 1

                if next_row == -1:  # 위에 아무것도 없단 뜻
                    board[0][col] = board[row][col]
                    board[row][col] = 0

                elif (
                    board[next_row][col] == board[row][col]
                    and not board_merged[next_row][col]
                ):  # 숫자가 합쳐질 수 있는 경우
                    board[next_row][col] += board[row][col]
                    board_merged[next_row][col] = True
                    board[row][col] = 0
                else:  # 숫자가 합쳐질 수 없는 경우
                    board[next_row + 1][col] = board[row][col]
                    if next_row + 1 != row:  # 이동은 한 경우
                        board[row][col] = 0

    if direction == 1:
        for row in range(n - 2, -1, -1):
            for col in range(n):
                next_row = row + 1
                while next_row < n and board[next_row][col] == 0:
                    next_row += 1

                if next_row == n:  # 아래에 아무것도 없단 뜻
                    board[n - 1][col] = board[row][col]
                    board[row][col] = 0

                elif (
                    board[next_row][col] == board[row][col]
                    and not board_merged[next_row][col]
                ):  # 숫자가 합쳐질 수 있는 경우
                    board[next_row][col] += board[row][col]
                    board_merged[next_row][col] = True
                    board[row][col] = 0
                else:  # 숫자가 합쳐질 수 없는 경우
                    board[next_row - 1][col] = board[row][col]
                    if next_row - 1 != row:  # 이동은 한 경우
                        board[row][col] = 0

    if direction == 2:
        for col in range(1, n):
            for row in range(n):
                next_col = col - 1
                while next_col >= 0 and board[row][next_col] == 0:
                    next_col -= 1
                if next_col == -1:  # 왼쪽에 아무것도 없단 뜻
                    board[row][0] = board[row][col]
                    board[row][col] = 0
                elif (
                    board[row][next_col] == board[row][col]
                    and not board_merged[row][next_col]
                ):  # 숫자가 합쳐질 수 있는 경우
                    board[row][next_col] += board[row][col]
                    board_merged[row][next_col] = True
                    board[row][col] = 0
                else:  # 숫자가 합쳐질 수 없는 경우
                    board[row][next_col + 1] = board[row][col]
                    if next_col + 1 != col:  # 이동은 한 경우
                        board[row][col] = 0
    if direction == 3:
        for col in range(n - 2, -1, -1):
            for row in range(n):
                next_col = col + 1
                while next_col < n and board[row][next_col] == 0:
                    next_col += 1
                if next_col == n:  # 오른쪽에 아무것도 없단 뜻
                    board[row][n - 1] = board[row][col]
                    board[row][col] = 0
                elif (
                    board[row][next_col] == board[row][col]
                    and not board_merged[row][next_col]
                ):  # 숫자가 합쳐질 수 있는 경우
                    board[row][next_col] += board[row][col]
                    board_merged[row][next_col] = True
                    board[row][col] = 0
                else:  # 숫자가 합쳐질 수 없는 경우
                    board[row][next_col - 1] = board[row][col]
                    if next_col - 1 != col:  # 이동은 한 경우
                        board[row][col] = 0


def solve(board, move_cnt):  # 지금까지 움직인 횟수이다.
    global max_block
    if move_cnt == 5:
        for line in board:
            max_block = max(max_block, max(line))  # 가장큰 블록을 찾는다.
        return

    for i in range(4):
        new_board = copy.deepcopy(board)
        move(new_board, i)
        solve(new_board, move_cnt + 1)


solve(board, 0)
print(max_block)
