import sys

input = sys.stdin.readline
move = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # 하, 상, 우, 좌 이동 의미
n, cow, road = map(int, input().strip().split())
board = [[0] * n for _ in range(n)]
# i, j에서 1은 i, j-1(세로) 부분이 막힌걸 의미
block_col = [[0] * n for _ in range(n)]
# i, j에서 1은 i-1, j(가로) 부분이 막힌걸 의미
block_row = [[0] * n for _ in range(n)]

conneted_cow = 0
cow_num = 3


def dfs(my_row, my_col):
    global conneted_cow
    stack = []
    stack.append([my_row, my_col])
    visited = [[False] * n for _ in range(n)]
    visited[my_row][my_col] = True
    while stack:
        row, col = stack.pop()

        for m in move:
            new_row = row + m[0]
            new_col = col + m[1]

            if new_col < 0 or new_col >= n or new_row < 0 or new_row >= n:
                continue

            if block_row[row][col] == 1 and m[0] == -1:  # 가로벽이고 위로 올라갈라 할 때
                continue

            if block_row[new_row][new_col] == 1 and m[0] == 1:  # 가로벽이고 위에서 내려왔을 때
                continue

            if block_col[row][col] == 1 and m[1] == -1:  # 세로벽이고 왼쪽으로 가려 할때
                continue

            if block_col[new_row][new_col] == 1 and m[1] == 1:  # 세로벽이고 왼쪽에서 왔을 때
                continue

            if not visited[new_row][new_col]:
                stack.append([new_row, new_col])
                visited[new_row][new_col] = True
                if board[new_row][new_col] == cow_num:  # 방문한 곳에 소가 있으면
                    if (new_row == my_row and new_col > my_col) or (
                        new_row > my_row
                    ):  # 전엔 세지 않았던 연결된 소이면
                        conneted_cow += 1


for _ in range(road):
    r1, c1, r2, c2 = map(lambda i: int(i) - 1, input().strip().split())
    if r1 == r2:  # 세로벽이다
        col = max(c1, c2)
        block_col[r1][col] = 1
    else:  # 가로벽이다.
        row = max(r1, r2)
        block_row[row][c1] = 1

for _ in range(cow):  # 소는 1부터 cow까지 진행한다
    r, c = map(lambda i: int(i) - 1, input().strip().split())
    board[r][c] = cow_num

for i in range(n):
    for j in range(n):
        if board[i][j] == cow_num:
            dfs(i, j)

total_pair = (cow * (cow - 1)) // 2

print(total_pair - conneted_cow)
