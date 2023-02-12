import math
from collections import deque

def privateLcm(a, b):
    return (a * b) // math.gcd(a, b)

def lcm(integers):
    cur_lcm = 1
    for i in integers:
        cur_lcm = privateLcm(cur_lcm, i)
    return cur_lcm

def makeTree(edges):
    sorted_edges = sorted(edges, key = lambda x: x[1])
    last_node = len(edges) + 1
    tree = [deque([]) for _ in range(last_node + 1)]
    for s, e in sorted_edges:
        tree[s].append(e)
    return tree

def getCycle(tree, root):
    if(len(tree[root]) == 0): #child node인 경우
        return 1
    cycles = []
    for child in tree[root]:
        cycles.append(getCycle(tree, child))
    return lcm(cycles) * len(tree[root])

def getChildeNode(tree):
    curNode = 1
    while(len(tree[curNode]) != 0):
        temp = tree[curNode].popleft()
        tree[curNode].append(temp)
        curNode = temp
    return curNode

def getCycleContent(cycle, tree):
    content = []
    while cycle > 0:
        content.append(getChildeNode(tree))
        cycle -= 1
    return content
        
def isExceeded(target, count_dict):
    for k, v in count_dict.items():
        if(target[k - 1] < v):
            return True
    return False

def isLack(target, count_dict):
    for idx, t in enumerate(target):
        if (idx + 1 not in count_dict and t > 0) or (idx + 1 in count_dict and t > count_dict[idx + 1] * 3):
            return True
    return False

def makeDictQuickCombination(number, cnt):
    arr = deque([])
    while cnt > 0:
        if (number - 1) <= (cnt - 1) * 3:
            number -= 1
            arr.append(1)
        elif (number - 2) <= (cnt - 1) * 3:
            number -= 2
            arr.append(2)
        else:
            number -= 3
            arr.append(3)
        cnt -= 1
    return arr
        
def solution(edges, target):
    tree = makeTree(edges)
    cycleNumber = getCycle(tree, 1)
    cycleContent = getCycleContent(cycleNumber, tree)
    count_dict = {}
    cycleContentSet = set(cycleContent)
    for idx, t in enumerate(target):
        if idx + 1 not in cycleContentSet and t > 0:
            return [-1]

    cur_pos = 0
    cnt = 0
    while True:
        if isExceeded(target, count_dict):
            return [-1]
        if not isLack(target, count_dict):
            combi_dict = {}
            for k, v in count_dict.items():
                combi_dict[k] = makeDictQuickCombination(target[k - 1], v)
            ans = []
            for i in range(cnt):
                ans.append(combi_dict[cycleContent[i % cycleNumber]].popleft())
            return ans
        
        if cycleContent[cur_pos] not in count_dict:
            count_dict[cycleContent[cur_pos]] = 1
        else:
            count_dict[cycleContent[cur_pos]] += 1
        
        cur_pos = (cur_pos + 1) % cycleNumber
        cnt += 1