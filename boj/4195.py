import sys

input = sys.stdin.readline
t = int(input())
def find(dic, name):
    if dic[name][0] == name:
        return name
    dic[name][0] = find(dic, dic[name][0])
    return dic[name][0]

def union(dic, nm1, nm2):
    nm1r = find(dic, nm1)
    nm2r = find(dic, nm2)
    if nm1r != nm2r:
        dic[nm1r][0] = nm2r
        dic[nm2r][1] += dic[nm1r][1]
        
    return dic[nm2r][1]        
for _ in range(t):
    n = int(input())
    set_dic = {}
    for _ in range(n):
        f1, f2 = input().split()
        if f1 not in set_dic:
            set_dic[f1] = [f1, 1]
        if f2 not in set_dic:
            set_dic[f2] = [f2, 1]
        print(union(set_dic, find(set_dic, f1), find(set_dic, f2)))