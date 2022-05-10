import sys

input = sys.stdin.readline
n = int(input())
set_num = 1 << 20
for _ in range(n):
    op = input().strip()
    if op != "all" and op != "empty":
        op, num = op.split()
    if op == "add":
        num = int(num) - 1
        set_num = set_num | 1 << num
    elif op == "remove":
        num = int(num) - 1
        set_num = set_num & ~(1 << num)
    elif op == "check":
        num = int(num) - 1
        if set_num >> num & 1:
            print(1)
        else:
            print(0)
    elif op == "toggle":
        num = int(num) - 1
        if set_num >> num & 1:
            set_num = set_num & ~(1 << num)
        else:
            set_num = set_num | 1 << num
    elif op == "all":
        set_num = ~(1 << 20)
    else:
        set_num = 1 << 20
