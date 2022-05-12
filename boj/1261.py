"""
BFS와 다익스트라 모두로 풀 수 있다.
1. 다익스트라 풀이
벽을 부수는 횟수에 제한이 없기 때문에 벽이 있는 부분을 간선의 가중치가 1, 없으면 0인 그래프라 생각하고
(0, 0) 에서 (M, N) 까지의 최소거리를 다익스트라 알고리즘을 통해 구하면 된다.

2. BFS 풀이
처음 고민했던 것. 재방문했을 때, 전에 방문했을 때 보다 적은 횟수로 벽을 부수고 오면 업데이트 해줘야 하나?
재방문의 경우를 고민했다.
해결법으론 벽이 없는 통로는 큐의 앞에 쌓아 두고, 벽이 있는 통로는 큐의 뒤쪽부터 쌓아둔다.
이러면 벽이 없는 통로로 쭉 돌고, 벽이 있는 통로를 돌기 때문에 dist를 단 한 번만 업데이트 해줘도 벽을 부순 최소 횟수임이 보장된다.
0과 1의 가중치가 있는 BFS이기 떄문에 0-1 BFS라고도 하는 것 같다.
이동의 가중치가 0과 1일 때 최소의 가중치로 움직이기 위한 방법
"""
from collections import deque

n, m = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(m)]
dist = [[-1] * n for _ in range(m)]

q = deque([(0, 0)])  # 위치, 벽을 부순 횟수를 의미한다.
dist[0][0] = 0  # 0번 벽을 부순 녀석이 방문함을 의미
move = [[0, 1], [0, -1], [1, 0], [-1, 0]]

while q:
    r, c = q.popleft()
    for mo in move:
        next_r = r + mo[0]
        next_c = c + mo[1]
        if next_r < 0 or next_r >= m or next_c < 0 or next_c >= n:
            continue

        if dist[next_r][next_c] != -1:  # 이미 방문함
            continue

        if board[next_r][next_c] == 1:
            q.append((next_r, next_c))
            dist[next_r][next_c] = dist[r][c] + 1
        else:
            q.appendleft((next_r, next_c))
            dist[next_r][next_c] = dist[r][c]


print(dist[m - 1][n - 1])
