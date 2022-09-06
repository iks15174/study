import sys

input = sys.stdin.readline
n = int(input())
depth_width = {}


class node:
    def __init__(self, num):
        self.val = num
        self.left = None
        self.right = None

    def add_left(self, node):
        self.left = node

    def add_right(self, node):
        self.right = node

    def cnt_total(self):
        self.total = self.cnt_left_node() + self.cnt_right_node() + 1
        return self.total

    def cnt_left_node(self):
        if self.left:
            self.left_cnt = self.left.cnt_total()
        else:
            self.left_cnt = 0
        return self.left_cnt

    def cnt_right_node(self):
        if self.right:
            self.right_cnt = self.right.cnt_total()
        else:
            self.right_cnt = 0
        return self.right_cnt

    def record_width(self, depth, start):
        global depth_width
        if depth not in depth_width:
            depth_width[depth] = {
                "min": start + self.left_cnt + 1,
                "max": start + self.left_cnt + 1,
            }
        else:
            depth_width[depth]["min"] = min(
                depth_width[depth]["min"], start + self.left_cnt + 1
            )
            depth_width[depth]["max"] = max(
                depth_width[depth]["max"], start + self.left_cnt + 1
            )
            
        if self.left:
            self.left.record_width(depth + 1, start)
        if self.right:
            self.right.record_width(depth + 1, start + self.left_cnt + 1)


node_set = {}
is_root = [True] * (n + 1)
is_root[0] = False
for _ in range(n):
    c, l, r = map(int, input().split())
    if r != -1:
        is_root[r] = False
    if l != -1:
        is_root[l] = False
    if c not in node_set:
        cur_node = node(c)
        node_set[c] = cur_node
    else:
        cur_node = node_set[c]
    if r not in node_set and r != -1:
        right = node(r)
        node_set[r] = right
    elif r != -1:
        right = node_set[r]
    else:
        right = None
    if l not in node_set and l != -1:
        left = node(l)
        node_set[l] = left
    elif l != -1:
        left = node_set[l]
    else:
        left = None
    cur_node.add_left(left)
    cur_node.add_right(right)

root = is_root.index(True)
node_set[root].cnt_total()
node_set[root].record_width(1, 0)

d = 0
w = 0
for k, i in depth_width.items():
    val = i["max"] - i["min"] + 1
    if val > w:
        d = k
        w = val
print(d, w)
