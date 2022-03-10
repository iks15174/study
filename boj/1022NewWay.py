r1, c1, r2, c2 = map(int, input().split())
row_len = (r2 - r1) + 1
col_len = (c2 - c1) + 1
result = [[0] * col_len for _ in range(row_len)]


def solve(r, c):
    if r == 0 and c == 0:
        return 1
    shell = max(abs(r), abs(c))
    size = shell * 2 + 1

    # 껍질의 상,하,좌,우 어디에 속하는지 케이스를 나눈다.
    if abs(r) == shell and r < 0:
        mid = (size - 2) ** 2 + size - 1 + shell
        return mid - c
    if abs(r) == shell and r > 0:
        mid = (size - 2) ** 2 + 3 * (size - 1) + shell
        return mid + c
    if abs(c) == shell and c < 0:
        mid = (size - 2) ** 2 + 2 * (size - 1) + shell
        return mid + r
    if abs(c) == shell and c > 0:
        mid = (size - 2) ** 2 + shell
        return mid - r


max_len = -1
for r in range(r1, r2 + 1):
    for c in range(c1, c2 + 1):
        result_num = str(solve(r, c))
        max_len = max(max_len, len(result_num))
        result[r - r1][c - c1] = result_num

for line in result:
    formmated_line = [str(num).rjust(max_len) for num in line]
    print(*formmated_line)
