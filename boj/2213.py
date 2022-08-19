n = int(input())
w = list(map(int, input().split()))
dp = [[0] * (n + 1) for _ in range(2)]
trace = [[[] for _ in range(n + 1)] for _ in range(2)]
visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]
ans = []
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def get_independent_set(cur):
    global dp, visited, graph, w, n, trace
    visited[cur] = True
    dp[1][cur] = w[cur - 1]
    for node in graph[cur]:
        if not visited[node]:
            get_independent_set(node)
            if dp[1][node] > dp[0][node]:
                trace[0][cur].append((node, 1))
            else:
                trace[0][cur].append((node, 0))
            dp[0][cur] += max(dp[1][node], dp[0][node])
            trace[1][cur].append((node, 0))
            dp[1][cur] += dp[0][node]
            
def get_trace(cur, used):
    global dp, visited, graph, w, n, trace, ans
    visited[cur] = True
    if used == 1:
        ans.append(cur)
    for node, n_used in trace[used][cur]:
        if not visited[node]: 
            get_trace(node, n_used)
        

      
get_independent_set(1)      
print(max(dp[0][1], dp[1][1]))
visited = [False] * (n + 1)
if dp[0][1] > dp[1][1]:
    get_trace(1, 0)
else:
    get_trace(1, 1)
ans = sorted(ans)
print(" ".join(map(str, ans)))