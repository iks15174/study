from collections import deque

n = int(input())
graph = []
for i in range(n):
    graph.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, colors, visited):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if graph[nx][ny] in colors and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))


# 적록색명이 아닐때
visited = [[False for _ in range(n)] for _ in range(n)]
not_color_blindness = 0
color_blindness = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, graph[i][j], visited)
            not_color_blindness += 1


# 적록색명일 때
visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            if graph[i][j] == "R" or graph[i][j] == "G":
                bfs(i, j, ["R", "G"], visited)
            else:
                bfs(i, j, graph[i][j], visited)
            color_blindness += 1

print(" ".join(map(str, [not_color_blindness, color_blindness])))
