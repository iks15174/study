n, m = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(n)]
numbering = [[-1] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
move = [[0, 1], [0, -1], [1, 0], [-1, 0]]

"""
풀이 핵심 : 
처츰에는 모든 1로부터 시작해 갈 수 있는 길을 세고 있었다.
문제점은 매번 1000 * 1000 크기의 visited 배열을 초기화해야 해서 시간초과가 났다

해결법
1이 아닌 0을 기준으로 생각하자. 현재 board는 벽에 의해 영역 별로 나누어져 있다.
각 영역의 id와 영역의 넓이 정보를 가지는 배열을 만들자
visited 배열을 최초에 한번만 초기화 하면 된다.
"""


def bfs(r, c, id):
    global visited
    cnt = 1
    visited[r][c] = True
    numbering[r][c] = id
    q = [(r, c)]
    while q:
        r, c = q.pop()
        for mo in move:
            next_r = r + mo[0]
            next_c = c + mo[1]
            if next_r < 0 or next_r >= n or next_c < 0 or next_c >= m:
                continue
            if board[next_r][next_c] == 0 and not visited[next_r][next_c]:
                visited[next_r][next_c] = True
                q.append((next_r, next_c))
                numbering[next_r][next_c] = id
                cnt += 1

    return cnt


id = 0
id_cnt = []
for row in range(n):
    for col in range(m):
        if board[row][col] == 0 and not visited[row][col]:
            id_cnt.append(bfs(row, col, id))
            id += 1

for row in range(n):
    for col in range(m):
        if board[row][col] == 1:
            add_item = set()
            for mo in move:
                next_r = row + mo[0]
                next_c = col + mo[1]
                if (
                    next_r < 0
                    or next_r >= n
                    or next_c < 0
                    or next_c >= m
                    or numbering[next_r][next_c] == -1
                ):
                    continue
                add_item.add(numbering[next_r][next_c])
            for a in add_item:
                board[row][col] += id_cnt[a]
                board[row][col] %= 10

for line in board:
    print("".join(map(str, line)))
