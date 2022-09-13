import sys

input = sys.stdin.readline
n, c = map(int, input().split())
m = int(input())
boxes = []
for _ in range(m):
    a, b, w = map(int, input().split())
    boxes.append([a, b, w])
    
boxes = sorted(boxes, key = lambda x : (x[1], x[0], x[2]))
vbox = [0] * (n + 1)
ans = 0
for s, e, w in boxes:
    temp = 0
    for r in range(s, e):
        temp = max(temp, vbox[r])
    load = w
    if c - temp < w:
        load = c - temp
    for r in range(s, e):
        vbox[r] += load
    ans += load
print(ans)