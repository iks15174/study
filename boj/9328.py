import string

test_case = int(input())
move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for _ in range(test_case):
    ans = 0
    row, col = map(int, input().split())
    visited = [[False] * col for _ in range(row)]
    board = [list(str(input())) for _ in range(row)]
    visit_postion = []  # 진입할 수 있는 지점을 의미
    keys = {}  # 현재 가지고 있는 key 의미
    doors = {}  # 현재 막혀있는 문 의미

    for s in string.ascii_lowercase:
        keys[s] = 0
    for s in string.ascii_uppercase:
        doors[s] = []

    for c in range(col):
        if (
            board[0][c] == "."
            or board[0][c] == "$"
            or board[0][c] in string.ascii_lowercase
        ):
            visit_postion.append((0, c))
            visited[0][c] = True
            if board[0][c] in string.ascii_lowercase:
                keys[board[0][c]] = 1
            if board[0][c] == "$":
                ans += 1
        if (
            board[row - 1][c] == "."
            or board[row - 1][c] == "$"
            or board[row - 1][c] in string.ascii_lowercase
        ):
            visit_postion.append((row - 1, c))
            visited[row - 1][c] = True
            if board[row - 1][c] in string.ascii_lowercase:
                keys[board[row - 1][c]] = 1
            if board[row - 1][c] == "$":
                ans += 1

        if board[row - 1][c] in string.ascii_uppercase:
            doors[board[row - 1][c]].append((row - 1, c))
        if board[0][c] in string.ascii_uppercase:
            doors[board[0][c]].append((0, c))

    for r in range(row):
        if (
            board[r][0] == "."
            or board[r][0] == "$"
            or board[r][0] in string.ascii_lowercase
        ) and not visited[r][0]:
            visit_postion.append((r, 0))
            visited[r][0] = True
            if board[r][0] in string.ascii_lowercase:
                keys[board[r][0]] = 1
            if board[r][0] == "$":
                ans += 1
        if (
            board[r][col - 1] == "."
            or board[r][col - 1] == "$"
            or board[r][col - 1] in string.ascii_lowercase
        ) and not visited[r][col - 1]:
            visit_postion.append((r, col - 1))
            visited[r][col - 1] = True
            if board[r][col - 1] in string.ascii_lowercase:
                keys[board[r][col - 1]] = 1
            if board[r][col - 1] == "$":
                ans += 1

        if board[r][0] in string.ascii_uppercase:
            doors[board[r][0]].append((r, 0))
        if board[r][col - 1] in string.ascii_uppercase:
            doors[board[r][col - 1]].append((r, col - 1))

    inital_keys = str(input())
    if not inital_keys == "0":
        inital_keys = list(inital_keys)
        for k in inital_keys:
            keys[k] = 1

    for k, v in keys.items():
        if v == 1:
            for d in doors[k.upper()]:
                visited[d[0]][d[1]] = True
                visit_postion.append(d)

    while visit_postion:
        pos = visit_postion.pop()
        for m in move:
            next_r = pos[0] + m[0]
            next_c = pos[1] + m[1]

            if (
                next_r < 0
                or next_r >= row
                or next_c < 0
                or next_c >= col
                or board[next_r][next_c] == "*"
            ):
                continue
            if board[next_r][next_c] in string.ascii_uppercase:
                if keys[board[next_r][next_c].lower()] == 1:  # 문에 해당하는 key가 있을 경우
                    if not visited[next_r][next_c]:
                        visited[next_r][next_c] = True
                        visit_postion.append((next_r, next_c))
                else:
                    doors[board[next_r][next_c]].append((next_r, next_c))

            elif board[next_r][next_c] in string.ascii_lowercase:
                if keys[board[next_r][next_c]] != 1:  # 존재하던 key 아닐 경우
                    keys[board[next_r][next_c]] = 1
                    for d in doors[board[next_r][next_c].upper()]:
                        visited[d[0]][d[1]] = True
                        visit_postion.append(d)

                    visited[next_r][next_c] = True
                    visit_postion.append((next_r, next_c))
                elif not visited[next_r][next_c]:
                    visited[next_r][next_c] = True
                    visit_postion.append((next_r, next_c))

            elif board[next_r][next_c] == "$" and not visited[next_r][next_c]:
                ans += 1
                visited[next_r][next_c] = True
                visit_postion.append((next_r, next_c))

            elif board[next_r][next_c] == "." and not visited[next_r][next_c]:
                visited[next_r][next_c] = True
                visit_postion.append((next_r, next_c))

    print(ans)
