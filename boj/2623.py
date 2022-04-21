idol_num, pd_num = map(int, input().split())
connected_node = [0] * (idol_num + 1)  # 자기에게 연결된 노드의 수를 의미한다.
graph = [[] for _ in range(idol_num + 1)]
for _ in range(pd_num):
    info = list(map(int, input().split()))
    for i in range(2, len(info)):
        connected_node[info[i]] += 1

    for i in range(1, len(info) - 1):
        graph[info[i]].append(info[i + 1])

zero_node = []  # 자기를 가리키는 녀석이 0인 노드이다.
for idx, cn in enumerate(connected_node):
    if cn == 0 and idx != 0:
        zero_node.append(idx)
result = []
while zero_node:
    node = zero_node.pop()
    result.append(node)
    for g in graph[node]:
        connected_node[g] -= 1
        if connected_node[g] == 0:
            zero_node.append(g)

if len(result) == idol_num:
    for r in result:
        print(r)
else:
    print(0)
