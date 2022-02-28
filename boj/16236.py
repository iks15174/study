from collections import deque

n = int(input())
board = [[] for _ in range(n)]
shark_size = 2  # 상어의 크기
shark_pos = [0, 0]  # 상어 위치
shark_eat_num = 0  # 상어가 먹이를 먹은 횟수
eatable = []  # 먹을 수 있는 먹이(y, x), 가장 가까운 먹이들만 들어간다.
move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
second = 0


def bfs():  # 상어의 현재 위취에서 가장 가까운 먹이를 찾는다.
    min_distance = -1  # 상어와 먹이의 최소거리
    queue = deque()  # 큐에 이동할 수 있는 위치와 이동 횟수를 함께 저장한다.
    queue.append((shark_pos, 0))
    visited = [[False] * n for _ in range(n)]
    while queue:
        q, dist = queue.popleft()
        if not visited[q[0]][q[1]]:
            visited[q[0]][q[1]] = True
            if (
                board[q[0]][q[1]] != 0
                and board[q[0]][q[1]] != 9
                and board[q[0]][q[1]] < shark_size
                and min_distance == -1
            ):  # 가장 가까운 먹이를 찾았을 때
                eatable.append(q)
                min_distance = dist
            if (
                board[q[0]][q[1]] != 0
                and board[q[0]][q[1]] != 9
                and board[q[0]][q[1]] < shark_size
                and min_distance != -1
            ):  # 먹이를 찾았을 때
                if (dist) == min_distance:  # 가장 가까운 먹이일 때
                    eatable.append(q)

            for m in move:
                next_y = q[0] + m[0]
                next_x = q[1] + m[1]
                if (
                    next_x >= 0 and next_x < n and next_y >= 0 and next_y < n
                ):  # 범위를 벗어나지 않을 때
                    if board[next_y][next_x] <= shark_size:  # 물고기가 있다면 상어의 크기와 같거나 작을 때
                        queue.append(([next_y, next_x], dist + 1))
    return min_distance


def find_best_fish():  # eatable 리스트에서 최적의 먹이를 찾는 함수
    global eatable
    eatable = sorted(
        eatable, key=lambda eat: (eat[0], eat[1])
    )  # y가 작으면서(가장 위), x가 작은(왼쪽) 순으로 정렬한다.
    if len(eatable) > 0:
        return eatable[0]
    else:
        return None


# 입력을 받는다.
for i in range(n):
    line = list(map(int, input().split()))
    board[i] = line
    for idx, l in enumerate(line):
        if l == 9:
            shark_pos[0] = i
            shark_pos[1] = idx

# 먹이 찾기를 시작한다.
while True:
    min_dist = bfs()  # 먹이 후보를 얻는다.
    best_fish = find_best_fish()  # 최적의 먹이를 찾는다.
    if not best_fish:  # 최적의 먹이가 없으면 더 이상 먹을게 없는 거다.
        break
    # 먹이를 먹고 먹이는 0으로 만들고, 상어의 위치를 바꿔준다.
    second += min_dist
    board[shark_pos[0]][shark_pos[1]] = 0
    shark_pos[0] = best_fish[0]
    shark_pos[1] = best_fish[1]
    board[best_fish[0]][best_fish[1]] = 9
    # 먹이를 먹으면 상어의 먹은 횟수가 증가한다.
    shark_eat_num += 1
    if shark_eat_num == shark_size:
        shark_size += 1
        shark_eat_num = 0
    # 먹이후보는 상어 위치가 바뀌었기 때문에 초기화 한다.
    eatable = []

print(second)
