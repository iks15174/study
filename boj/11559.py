from collections import deque

puyo_board = [[] for _ in range(12)]
for i in range(12):
    puyo_board[i] = list(input())
chain_num = 0  # 연쇄 숫자이다.
move = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def find_explore(y, x):  # 찾기 시작할 y, x를 의미한다.  폭파될 칸은 E로 표시한다.
    color = puyo_board[y][x]
    visited = [[False] * 6 for _ in range(12)]
    result = []  # 폭파시킬 것들을 담는 배열이다.
    q = deque()
    q.append([y, x])
    result.append([y, x])
    visited[y][x] = True
    while q:
        cur_y, cur_x = q.popleft()
        for mo in move:
            next_y = cur_y + mo[0]
            next_x = cur_x + mo[1]
            if next_y < 0 or next_y >= 12 or next_x < 0 or next_x >= 6:
                continue
            if puyo_board[next_y][next_x] == color and not visited[next_y][next_x]:
                visited[next_y][next_x] = True
                q.append([next_y, next_x])
                result.append([next_y, next_x])
    if len(result) >= 4:  # 4개 이상이면 폭파시킨다.
        for node in result:
            puyo_board[node[0]][node[1]] = "E"


def remove_block():
    removed = 0  # 삭제된 블럭 갯수, 0개이면 연쇄가 끝난 것이다.
    # E로 표시된 것들을 삭제한다.
    for i in range(12):
        for j in range(6):
            if puyo_board[i][j] == "E":
                removed += 1
                puyo_board[i][j] = "."

    # 블럭을 아래로 내려준다.
    for j in range(6):
        new_board = ["."] * 12
        new_board_idx = 11
        for i in range(11, -1, -1):
            if puyo_board[i][j] != ".":
                new_board[new_board_idx] = puyo_board[i][j]
                new_board_idx -= 1
        # puyoboard 업데이트
        for i in range(12):
            puyo_board[i][j] = new_board[i]
    return removed


while True:
    for i in range(12):
        for j in range(6):
            if puyo_board[i][j] != "." and puyo_board[i][j] != "E":
                find_explore(i, j)

    removed = remove_block()
    if removed > 0:
        chain_num += 1
    else:
        break
print(chain_num)
