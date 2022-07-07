from collections import deque
def solution(board):
    HORIZON = 1
    VERT = 0
    answer = 0
    N = len(board)
    move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    visited = [[ set() for _ in range(N)] for _ in range(N)]
    visited[0][0].add(HORIZON)
    visited[0][1].add(HORIZON)
    q = deque([[[0, 0], [0, 1], 0]])
    while q:
        first, second, dist = q.popleft()
        # print(first, second, dist)
        direction = HORIZON
        if first[1] == second[1]:
            direction = VERT
        
        for m in move:
            fr = first[0] + m[0]
            fc = first[1] + m[1]
            sr = second[0] + m[0]
            sc = second[1] + m[1]
            if fr < 0 or fr >= N or fc < 0 or fc >= N or sr < 0 or sr >= N or sc < 0 or sc >= N:
                continue
            if (direction not in visited[fr][fc] or direction not in visited[sr][sc]) and board[fr][fc] == 0 and board[sr][sc] == 0:
                if (fr == N - 1 and fc == N - 1) or (sr == N - 1 and sc == N - 1):
                    return dist + 1
                visited[fr][fc].add(direction)
                visited[sr][sc].add(direction)
                q.append([[fr, fc], [sr, sc], dist + 1])
        
        for i in range(2):
            rot = direction * 2 + i
            rotfr = first[0] + move[rot][0]
            rotfc = first[1] + move[rot][1]
            rotsr = second[0] + move[rot][0]
            rotsc = second[1] + move[rot][1]
            
            cur_dir = 1 - direction
            
            if rotfr < 0 or rotfr >= N or rotfc < 0 or rotfc >= N or rotsr < 0 or rotsr >= N or rotsc < 0 or rotsc >= N:
                continue
            
            if board[rotfr][rotfc] == 1 or board[rotsr][rotsc] == 1:
                continue
            
            if (cur_dir not in visited[first[0]][first[1]] or cur_dir not in visited[rotfr][rotfc]):
                if rotfr == N - 1 and rotfc == N - 1:
                    return dist + 1
                visited[first[0]][first[1]].add(cur_dir)
                visited[rotfr][rotfc].add(cur_dir)
                q.append([[first[0], first[1]], [rotfr, rotfc], dist + 1])
                
            
            if (cur_dir not in visited[second[0]][second[1]] or cur_dir not in visited[rotsr][rotsc]):
                if rotsr == N - 1 and rotsc == N - 1:
                    return dist + 1
                visited[second[0]][second[1]].add(cur_dir)
                visited[rotsr][rotsc].add(cur_dir)
                q.append([[second[0], second[1]], [rotsr, rotsc], dist + 1])
            
                
                
        
    return answer