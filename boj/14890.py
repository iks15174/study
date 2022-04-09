n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]


def solve(road):
    cnt = 1
    for i in range(len(road) - 1):
        if road[i] == road[i + 1]:
            cnt += 1
        elif road[i] - road[i + 1] == -1 and cnt >= l:  # 오르막길이다.
            cnt = 1
        elif road[i] - road[i + 1] == 1 and cnt >= 0:  # 내리막길이다.
            cnt = -l + 1
        else:
            return False
    if cnt < 0:
        return False
    return True


ans = 0
for b in board:  # 행의 길을 검사
    if solve(b):
        ans += 1

for i in range(n):
    col_list = []
    for j in range(n):
        col_list.append(board[j][i])
    if solve(col_list):
        ans += 1

print(ans)
