import math
import sys
sys.setrecursionlimit(2000)
nodeinfo = []
heights = []
node_by_height = {}
class Node:
    def __init__(self, x, y, val):
        self.name = val
        self.x = x
        self.y = y
    def set_left(self, left_node):
        self.left = left_node
    def set_right(self, right_node):
        self.right = right_node
    
def make_node(node, hidx, x_min, x_max):
    global nodeinfo, node_by_height, heights
    if hidx == len(heights):
        return None
    for name, x in node_by_height[heights[hidx]]:
        if x_min < x < x_max:
            new_node = Node(x, heights[hidx], name)
            new_node.set_left(make_node(new_node, hidx + 1, x_min, x))
            new_node.set_right(make_node(new_node, hidx + 1, x, x_max))
            return new_node
    return None

def prio_search(node, result):
    if node:
        result.append(node.name)
        prio_search(node.left, result)
        prio_search(node.right, result)
        
def post_search(node, result):
    if node:
        post_search(node.left, result)
        post_search(node.right, result)
        result.append(node.name)
        
def solution(nodeinfop):
    global nodeinfo, node_by_height, heights
    for i in range(len(nodeinfop)):
        nodeinfop[i].append(i + 1)
    nodeinfo = sorted(nodeinfop, key=lambda n : (-n[1], n[0]))
    for x, y, name in nodeinfo:
        if y not in node_by_height:
            node_by_height[y] = [[name, x]]
            heights.append(y)
        else:
            node_by_height[y].append([name, x])
    heights = sorted(heights, reverse=True)
    root = Node(nodeinfo[0][0], nodeinfo[0][1], nodeinfo[0][2])
    root.set_left(make_node(root, 1, -math.inf, root.x))
    root.set_right(make_node(root, 1, root.x, math.inf))
    
    prio_result = []
    post_result = []
    prio_search(root, prio_result)
    post_search(root, post_result)
    return [prio_result, post_result]