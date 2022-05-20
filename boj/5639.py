import sys

sys.setrecursionlimit(20000)
input = sys.stdin.readline


class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, node):
        if self.val > node.val:
            if not self.left:
                self.left = node
            else:
                self.left.insert(node)
        else:
            if not self.right:
                self.right = node
            else:
                self.right.insert(node)


root = None
while True:
    try:
        val = input()
        if val == "":
            break
        val = int(val)
        if not root:
            root = node(val)
        else:
            root.insert(node(val))
    except EOFError:
        break


def back_print(node):
    if not node:
        return
    back_print(node.left)
    back_print(node.right)
    print(node.val)


back_print(root)
