import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n = int(input())
people = list(map(int, input().split()))
dp_con = [0] * (n + 1)
dp_ex = [0] * (n + 1)
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
root = 1
visited = [False] * (n + 1)

def solve(node):
    global visited, dp_ex, dp_con, people, tree
    dp_con[node] = people[node - 1]
    for c in tree[node]:
        if not visited[c]:
            visited[c] = True
            solve(c)
            dp_con[node] += dp_ex[c]
            dp_ex[node] += max(dp_con[c], dp_ex[c])
  
visited[root] = True      
solve(root)    
print(max(dp_con[root], dp_ex[root]))            
        