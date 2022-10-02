import sys
from collections import deque
input = sys.stdin.readline

# 입력을 받는다.
n, m = map(int, input().split())
move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
board = [[] for _ in range(n)]
for i in range(n):
    line = input().strip()
    board[i] = [int(l) for l in line]

# 첫번째는 벽을 부수고 방문했을 때 True로 바뀌고, 두번쨰는 벽을 안 부수고 방문했을 때 True로 바뀐다.
visited = [[[False, False] for _ in range(m)] for _ in range(n)]

# bfs를 위한 queue
queue = deque([])
queue.append([0, 0, 1])  # 각각 y, x좌표, 벽 부술 기회, 거리를 의미한다.
find = False
dist = 1
while queue:
    if find:
        break
    size = len(queue)
    for _ in range(size):
        y, x, brick_crush = queue.popleft()
        if y == n - 1 and x == m - 1:
            print(dist)
            find = True
            break
        for mo in move:
            next_y = y + mo[0]
            next_x = x + mo[1]
            if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                continue
            if board[next_y][next_x] == 0 and not visited[next_y][next_x][brick_crush]:
                queue.append([next_y, next_x, brick_crush])
                visited[next_y][next_x][brick_crush] = True
            if (
                board[next_y][next_x] == 1
                and brick_crush == 1
                and not visited[next_y][next_x][0]
            ):  # 벽을 부순상태에서 도달한 적이 없다면
                queue.append([next_y, next_x, 0])
                visited[next_y][next_x][0] = True
    dist += 1


if not find:
    print(-1)
