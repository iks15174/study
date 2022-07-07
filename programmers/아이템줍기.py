from collections import deque
def check_board(rectangle, cur_x, cur_y, prev_x, prev_y):
    for min_x, min_y, max_x, max_y in rectangle:
        if cur_x == prev_x and min_x < cur_x < max_x and min_y <= min(cur_y, prev_y) < max_y:
            return False
        if cur_y == prev_y and min_y < cur_y < max_y and min_x <= min(cur_x, prev_x) < max_x:
            return False
    for min_x, min_y, max_x, max_y in rectangle:
        # 어떤 사각형의 왼쪽 세로 테두리에 있을 때
        if cur_x == min_x and (min_y <= cur_y <= max_y):
            if prev_x == min_x and (min_y <= prev_y <= max_y):
                return True
            
        if cur_x == max_x and (min_y <= cur_y <= max_y):
            if prev_x == max_x and (min_y <= prev_y <= max_y):
                return True
        
        if cur_y == min_y and (min_x <= cur_x <= max_x):
            if prev_y == min_y and (min_x <= prev_x <= max_x):
                return True
            
        if cur_y == max_y and (min_x <= cur_x <= max_x):
            if prev_y == max_y and (min_x <= prev_x <= max_x):
                return True
    return False
            
def solution(rectangle, characterX, characterY, itemX, itemY):
    move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    q = deque([[characterX, characterY, 0]])
    visited = [[False] * 51 for _ in range(51)]
    visited[characterX][characterY] = True
    while q:
        cur_x, cur_y, dist = q.popleft()
        # print(cur_x, cur_y)
        for m in move:
            nx = cur_x + m[0]
            ny = cur_y + m[1]
            if nx < 1 or nx > 50 or ny < 1 or ny > 50:
                continue
            if not visited[nx][ny] and check_board(rectangle, nx, ny, cur_x, cur_y):
                if nx == itemX and ny == itemY:
                    return dist + 1
                visited[nx][ny] = True
                q.append([nx, ny, dist + 1])
            
