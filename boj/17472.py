import heapq
import sys

r, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
move = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 상 우 하 좌


def find(n1, connected):
    if n1 == connected[n1]:
        return n1
    connected[n1] = find(connected[n1], connected)
    return connected[n1]


def union(n1, n2, connected):
    n1_root = find(n1, connected)
    n2_root = find(n2, connected)

    if n1_root != n2_root:
        connected[n1_root] = n2_root


def seperate_island(i, j, board, island_id):
    global r, c, move
    board[i][j] = island_id
    q = [[i, j]]
    while q:
        cr, cc = q.pop()
        for m in move:
            nr = cr + m[0]
            nc = cc + m[1]
            if nr < 0 or nr >= r or nc < 0 or nc >= c or board[nr][nc] != 1:
                continue
            board[nr][nc] = island_id
            q.append([nr, nc])


def is_outline(i, j, board, direction):
    global r, c, move
    if board[i][j] >= 2:
        nr = i + move[direction][0]
        nc = j + move[direction][1]
        if nr < 0 or nr >= r or nc < 0 or nc >= c or board[nr][nc] != 0:
            return False
        return True
    return False


def find_neighbor(i, j, board, direction):
    global r, c, move
    cur_id = board[i][j]
    i += move[direction][0]
    j += move[direction][1]
    dist = 0
    while board[i][j] == 0:
        i += move[direction][0]
        j += move[direction][1]
        if i < 0 or i >= r or j < 0 or j >= c:
            return [-1, -1]
        dist += 1
    if dist <= 1 or board[i][j] == cur_id:
        return [-1, -1]
    return [dist, board[i][j]]


island_id = 2  # 섬은 2부터 시작한다.
for i in range(r):
    for j in range(c):
        if board[i][j] == 1:
            seperate_island(i, j, board, island_id)
            island_id += 1

graph = []
for i in range(r):
    for j in range(c):
        if board[i][j] >= 2:
            for d in range(4):
                if is_outline(i, j, board, d):
                    dist, land = find_neighbor(i, j, board, d)
                    if dist != -1:
                        heapq.heappush(
                            graph, [dist, board[i][j], land]
                        )  # 거리, 시작, 끝 정보를 담고 있다.

# for b in board:
#     print(b)
# print(graph)
connection_info = [i for i in range(island_id)]
answer = 0
while graph:
    dist, start, end = heapq.heappop(graph)
    start_root = find(start, connection_info)
    end_root = find(end, connection_info)
    if start_root != end_root:
        union(start_root, end_root, connection_info)
        answer += dist

cur_root = find(2, connection_info)
for iland in range(3, island_id):
    if cur_root != find(iland, connection_info):
        print(-1)
        sys.exit()

print(answer)
