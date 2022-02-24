n = int(input())
relation = list(map(int, input().split()))
relation_num = int(input())

relation_table = [[] for _ in range(100 + 1)]
visited = [False for _ in range(100 + 1)]

for i in range(relation_num):
    n, m = map(int, input().split())
    relation_table[n].append(m)
    relation_table[m].append(n)

ans = -1


def dfs(depth, current_node):
    global ans
    visited[current_node] = True
    for i in relation_table[current_node]:
        if not visited[i] and i != relation[1]:
            dfs(depth + 1, i)
        elif i == relation[1]:
            ans = depth
            return


dfs(1, relation[0])
print(ans)
