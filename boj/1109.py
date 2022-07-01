import math
r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
'''
1. 각 섬을 나눈다.
2. 섬 주변에서 가장 낮은 수의 섬을 찾는다 -> 경계 탈출하면 -1 아니면 가장 낮은게 부모
3. 부모 정보를 담은 배열로 부터 높이를 구한다. 자신을 부모로 가지는 섬의 높이중 가장 큰 높이 + 1 -> 재귀와 dp로 해결 할 것
4. 내일의 나야 부탁해!
'''
ground = [[-1] * c for _ in range(r)]
g_num = 0

def dfs(row, col, g_num):
    global r, c, board, ground
    move = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    q = [[row, col]]
    visited = [[False] * c for _ in range(r)]
    visited[row][col] = True
    ground[row][col] = g_num
    while q:
        cr, cc = q.pop()
        for m in move:
            nr = cr + m[0]
            nc = cc + m[1]
            if nr < 0 or nr >= r or nc < 0 or nc >= c:
                continue
            if not visited[nr][nc] and board[nr][nc] == 'x':
                visited[nr][nc] = True
                ground[nr][nc] = g_num
                q.append([nr, nc])
                
def dfs_parent(row, col, my_num):
    global r, c, board, ground
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    q = [[row, col]]
    visited = [[False] * c for _ in range(r)]
    visited[row][col] = True
    ans = math.inf
    while q:
        cr, cc = q.pop()
        for m in move:
            nr = cr + m[0]
            nc = cc + m[1]
            if nr < 0 or nr >= r or nc < 0 or nc >= c:
                return -1
            if not visited[nr][nc] and (board[nr][nc] == '.' or ground[nr][nc] == my_num):
                visited[nr][nc] = True
                q.append([nr, nc])
            if board[nr][nc] == 'x' and ground[nr][nc] != my_num:
                ans = min(ans, ground[nr][nc])
    return ans
for row in range(r):
    for col in range(c):
        if board[row][col] == 'x' and ground[row][col] == -1:
            dfs(row, col, g_num)
            g_num += 1
            
parent = [-2] * g_num 
for row in range(r):
    for col in range(c):
        if ground[row][col] != -1 and parent[ground[row][col]] == -2:
            parent[ground[row][col]] = dfs_parent(row, col, ground[row][col])
            
height = [-1] * g_num            
def find_height(g):
    global parent, height
    if height[g] != -1:
        return height[g]
    
    ans = -2
    for idx, p in enumerate(parent):
        if p == g:
            ans = max(ans, find_height(idx))
    if ans == -2:
        height[g] = 0
        return height[g] 
    height[g] = ans + 1
    return height[g]

for g in range(g_num):
    height[g] = find_height(g)
    
if g_num == 0:
    print(-1)
else:
    for i in range(max(height) + 1):
        print(height.count(i), end=" ")