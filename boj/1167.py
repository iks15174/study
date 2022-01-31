n = int(input())

graph = [[] for _ in range(n + 1)]
max_diameter = -1
target_node = 0

for i in range(n):
    node_info = list(map(int, input().split()))
    node_info.pop()  # 마지막 -1 제거
    node = node_info.pop(0)  # 어떤 node 정보인지 얻기
    for j in range(0, len(node_info), 2):
        graph[node].append((node_info[j], node_info[j + 1]))  # 간선의 연결 정보를 저장


# sum은 현재까지의 거리의 총합.
# dfs 방식으로 그래프를 끝까지 타고 들어간 후 총합 거리(sum)이 기존값보다
# 크면 노드 및 sum을 업데이트 해준다.
def dfs(cur_node, from_node, sum):
    global target_node
    global max_diameter

    if (
        len(graph[cur_node]) == 1 and graph[cur_node][0][0] == from_node
    ):  # 더 이상 갈 곳이 없을 때
        if sum > max_diameter:
            target_node = cur_node
            max_diameter = sum
        return

    for connect_info in graph[cur_node]:
        if connect_info[0] == from_node:
            continue
        dfs(connect_info[0], cur_node, sum + connect_info[1])


dfs(2, 2, 0)  # 임의의 노드로부터 가장 먼 노드를 구한다.
max_diameter = -1  # 지름 값 초기화
dfs(target_node, target_node, 0)  # 가정 멀었던 노드로 부터 지름을 구한다.
print(max_diameter)
