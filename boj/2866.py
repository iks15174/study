import sys

input = sys.stdin.readline

r, c = map(int, input().split())
board = [input() for _ in range(r)]
same_pos = r
row_index = r - 1
col_strings = [""] * c
while row_index > 0:
    same_flag = False
    for col in range(c):
        col_strings[col] += board[row_index][col]
    temp_set = set()
    for col_string in col_strings:
        if col_string in temp_set:
            same_flag = True
            break
        temp_set.add(col_string)
    if same_flag:
        same_pos = row_index
    row_index -= 1

print(same_pos - 1)
