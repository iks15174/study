row, col = map(int, input().split())
board = [list(str(input())) for _ in range(row)]
sqaure_num = 0
move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
for r in range(row):
    for c in range(col):
        cur_color = board[r][c]
        expected_color = "B" if cur_color == "W" else "W"
        is_possible = True
        for m in move:
            next_r = r + m[0]
            next_c = c + m[1]
            if next_r < 0 or next_r >= row or next_c < 0 or next_c >= col:
                continue
            if board[next_r][next_c] == expected_color:
                is_possible = False
        if is_possible:
            sqaure_num += 1


def expent(num):
    if num == 0:
        return 1
    if num % 2 == 0:
        prod = expent(num // 2)
        prod = prod * prod
        prod %= 1000000007
        return prod
    else:
        prod = 2 * expent(num - 1)
        prod %= 1000000007
        return prod


print(expent(sqaure_num))
