import sys

sys.setrecursionlimit(10 ** 6)
n = int(input())
trees = [[] for _ in range(n + 1)]  # 각 노드의 연결 정보를 저장한다. trees[i] -> i 부모노드의 연결정보
for _ in range(n - 1):
    line = list(map(int, input().split()))
    trees[line[0]].append([line[1], line[2]])  # 연결된 노드 및 간선 크기 저장
    trees[line[1]].append([line[0], line[2]])  # 양방향 저장

# 풀이는 루트로부터 가장 먼 곳을 찾는다 -> 지름의 한 끝점
circle_point = 0
max_weight = 0
visited = [False] * (n + 1)


def dfs(node, weight_sum):  # weight sum은 현재 노드에 도달할 떄까지의 간선 가중치의 합니다.
    global circle_point, max_weight, visited

    visited[node] = True
    if weight_sum > max_weight:
        max_weight = weight_sum
        circle_point = node
    for no in trees[node]:
        if not visited[no[0]]:
            dfs(no[0], weight_sum + no[1])


dfs(1, 0)  # 루트로부터 가장 먼 노드, 원의 지름의 한 끝부분 찾기
circle_first_point = circle_point  # 원의 끝부분 저장
circle_point = 0  # 초기화
max_weight = 0
visited = [False] * (n + 1)
dfs(circle_first_point, 0)
print(max_weight)
