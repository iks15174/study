# n, r, c = map(int, input().split())
# cur_len = 2 ** n
# start_num = 0
# while cur_len != 1:
#     if r < cur_len // 2 and c < cur_len // 2:
#         cur_len = cur_len // 2
#     elif r >= cur_len // 2 and c < cur_len // 2:
#         cur_len = cur_len // 2
#         start_num += (cur_len ** 2) * 2
#         r -= cur_len
#     elif r < cur_len // 2 and c >= cur_len // 2:
#         cur_len = cur_len // 2
#         start_num += cur_len ** 2
#         c -= cur_len
#     elif r >= cur_len // 2 and c >= cur_len // 2:
#         cur_len = cur_len // 2
#         start_num += (cur_len ** 2) * 3
#         r -= cur_len
#         c -= cur_len

# print(start_num)
n, r, c = map(int, input().split())
ans = 0
def solve(cr, cc, n, cnt):
    global r, c, ans
    if n == 1:
        ans = cnt + 2 * (r - cr) + (c - cc)
        return
    sub_line = (2 ** (n - 1))
    square = sub_line ** 2
    if cr <= r < cr + sub_line and cc <= c < cc + sub_line:
        solve(cr, cc, n - 1, cnt)
    elif cr <= r < cr + sub_line and cc + sub_line <= c < cc + 2 * sub_line:
        solve(cr, cc + sub_line, n - 1, cnt + square)
    elif cr + sub_line <= r < cr + 2 * sub_line and cc <= c < cc + sub_line:
        solve(cr + sub_line, cc, n - 1, cnt + 2 * square)
    else:
        solve(cr + sub_line, cc + sub_line, n - 1, cnt + 3 * square)
solve(0, 0, n, 0)
print(ans)
    
    
