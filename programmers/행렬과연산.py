from collections import deque

def rotate(left, middle, right):
    val = left.popleft()
    middle[0].appendleft(val)
    val = middle[0].pop()
    right.appendleft(val)
    val = right.pop()
    middle[-1].append(val)
    val = middle[-1].popleft()
    left.append(val)

def shift_row(left, middle, right):
    middle.appendleft(middle.pop())
    left.appendleft(left.pop())
    right.appendleft(right.pop())
    
def solution(rc, operations):
    left = deque([])
    middle = deque([])
    right = deque([])
    
    for r in range(len(rc)):
        left.append(rc[r][0])
        right.append(rc[r][-1])
    
    for r in range(len(rc)):
        temp = []
        for c in range(1, len(rc[0]) - 1, 1):
            temp.append(rc[r][c])
        middle.append(deque(temp))
        
    for op in operations:
        if op == "Rotate":
            rotate(left, middle, right)
        else:
            shift_row(left, middle, right)
            
    ans = []
    for r in range(len(rc)):
        temp = []
        temp.append(left[r])
        for c in range(0, len(rc[0]) - 2, 1):
            temp.append(middle[r][c])
        temp.append(right[r])
        ans.append(temp)
    return ans
        