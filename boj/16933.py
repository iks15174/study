from sys import stdin
from collections import deque


def visitable(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(start):
    q = deque([start])
    dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
    while q:

        cur_x, cur_y, wall, day, dist = q.popleft()
        if [cur_x, cur_y] == [n - 1, m - 1]:
            return dist
        for x, y in dirs:
            next_x, next_y = cur_x + x, cur_y + y
            if visitable(next_x, next_y):
                if not graph[next_x][next_y] and not visited[next_x][next_y][wall]:
                    visited[next_x][next_y][wall] = dist + 1
                    q.append((next_x, next_y, wall, not day, dist + 1))
                elif wall > 0 and not visited[next_x][next_y][wall - 1]:
                    if day:
                        visited[next_x][next_y][wall - 1] = dist + 1
                        q.append((next_x, next_y, wall - 1, not day, dist + 1))
                    else:
                        q.append((cur_x, cur_y, wall, not day, dist + 1))


    return -1


n, m, k = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().strip())) for _ in range(n)]
visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]
visited[0][0] = [1] * (k + 1)
print(bfs((0, 0, k, True, 1)))