r, c, k = map(int, input().split())
board = [[0] * c for _ in range(r)]
stickers = []
for _ in range(k):
    sticker_row, sticker_col = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(sticker_row)]
    stickers.append(sticker)


def rotate_90(square):
    row_len = len(square)
    col_len = len(square[0])
    rotated_square = [[0] * row_len for _ in range(col_len)]
    for r in range(row_len):
        for c in range(col_len):
            rotated_square[c][row_len - r - 1] = square[r][c]

    return rotated_square


def is_attach_possible(sticker, start_row, start_col):
    global board
    for r in range(start_row, start_row + len(sticker)):
        for c in range(start_col, start_col + len(sticker[0])):
            if board[r][c] == 1 and sticker[r - start_row][c - start_col] == 1:
                return False
    return True


def attach_sticker(sticker, start_row, start_col):
    global board
    cnt = 0
    for r in range(start_row, start_row + len(sticker)):
        for c in range(start_col, start_col + len(sticker[0])):
            if sticker[r - start_row][c - start_col] == 1:
                board[r][c] = 1
                cnt += 1

    return cnt


ans = 0
for sticker in stickers:
    attached = False
    for _ in range(4):
        if attached:
            break
        for s_r in range(r - len(sticker) + 1):
            if attached:
                break
            for s_c in range(c - len(sticker[0]) + 1):
                if is_attach_possible(sticker, s_r, s_c):
                    ans += attach_sticker(sticker, s_r, s_c)
                    attached = True
                    break
        sticker = rotate_90(sticker)

print(ans)
