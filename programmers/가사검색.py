import sys

sys.setrecursionlimit(10**5)
class Node:
    def __init__(self, val):
        self.val = val
        self.child_state = {}
        self.childs = []
    def set_child(self, child):
        self.childs.append(child)
    def update_state(self, length):
        if length in self.child_state:
            self.child_state[length] += 1
        else:
            self.child_state[length] = 1
def make_tree(parent, s, idx, d):
    if idx == len(s) or idx == -1:
        return
    state_key = len(s) - idx - 1 if d == 1 else idx
    for child in parent.childs:
        if child.val == s[idx]:
            child.update_state(state_key)
            make_tree(child, s, idx + d, d)
            return
    new_child = Node(s[idx])
    parent.set_child(new_child)
    new_child.child_state[state_key] = 1
    make_tree(new_child, s, idx + d, d)
    return
def get_num(parent, s, idx, d):
    if s[idx] != "?":
        for child in parent.childs:
            if child.val == s[idx]:
                return get_num(child, s, idx + d, d)
            
    else:
        cnt = 0
        for child in parent.childs:
            state_key = len(s) - idx - 1 if d == 1 else idx
            cnt += child.child_state[state_key] if state_key in child.child_state else 0
        return cnt
    return 0
     
def solution(words, queries):
    answer = []
    root = Node(-1)
    reverse_root = Node(-1)
    for word in words:
        make_tree(root, word, 0, 1)
        make_tree(reverse_root, word, len(word) - 1, -1)
    for q in queries:
        if q[0] == "?":
            answer.append(get_num(reverse_root, q, len(q) - 1, -1))
        else:
            answer.append(get_num(root, q, 0, 1))
    return answer
            
            
        
            