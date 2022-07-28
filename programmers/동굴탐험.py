def solution(n, path, order):
    tree = {i : [] for i in range(n)}
    orderd = { o[1] : o[0] for o in order }
    orderr = { o[0] : o[1] for o in order }
    visited = {i : False for i in range(n)}
    if 0 in orderd:
        return False
    for start, end in path:
        tree[start].append(end)
        tree[end].append(start)
    q = [0]
    temp_q = set()
    visited[0] = True
    while q:
        cur_node = q.pop()
        for next_node in tree[cur_node]:
            if visited[next_node]:
                continue
            if next_node in orderd and not visited[orderd[next_node]]:
                temp_q.add(next_node)
                continue
            q.append(next_node)
            visited[next_node] = True
            if next_node in orderr and orderr[next_node] in temp_q:
                temp_q.remove(orderr[next_node])
                q.append(orderr[next_node])
                visited[orderr[next_node]] = True
    if len(temp_q) != 0:
        return False
    return True
