n, r, c = map(int, input().split())
cur_len = 2 ** n
start_num = 0
while cur_len != 1:
    if r < cur_len // 2 and c < cur_len // 2:
        cur_len = cur_len // 2
    elif r >= cur_len // 2 and c < cur_len // 2:
        cur_len = cur_len // 2
        start_num += (cur_len ** 2) * 2
        r -= cur_len
    elif r < cur_len // 2 and c >= cur_len // 2:
        cur_len = cur_len // 2
        start_num += cur_len ** 2
        c -= cur_len
    elif r >= cur_len // 2 and c >= cur_len // 2:
        cur_len = cur_len // 2
        start_num += (cur_len ** 2) * 3
        r -= cur_len
        c -= cur_len

print(start_num)
