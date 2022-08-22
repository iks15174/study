import sys

input = sys.stdin.readline
m = int(input())
f = list(map(int, input().split()))
q = int(input())
table = [[0] * m for _ in range(23)]


def make_sparse_table():
    global m, f, table
    table[0] = f
    for i in range(1, 23):
        for j in range(m):
            table[i][j] = table[i - 1][table[i - 1][j] - 1]


make_sparse_table()
for _ in range(q):
    n, x = map(int, input().split())
    t_idx = 0
    cur_value = x
    while n > 0:
        if 1 & n:
            cur_value = table[t_idx][cur_value - 1]
        t_idx += 1
        n = n >> 1
    print(cur_value)
