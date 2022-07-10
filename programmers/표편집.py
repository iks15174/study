def solution(n, k, cmd):
    is_exist = [True] * n
    cur_pos = k
    removed = []
    next_pos = [i + 1 for i in range(n - 1)]
    prev_pos = [i -1 for i in range(n)]
    next_pos.append(-1) # next는 각 원소의 다음을 가리킨다.
    for c in cmd:
        if c == "C":
            is_exist[cur_pos] = False
            removed.append([cur_pos, prev_pos[cur_pos], next_pos[cur_pos]])
            if next_pos[cur_pos] == -1:
                prev = prev_pos[cur_pos]
                prev_pos[cur_pos] = -1
                next_pos[prev] = -1
                cur_pos = prev
            elif prev_pos[cur_pos] == -1:
                nextp = next_pos[cur_pos]
                prev_pos[nextp] = -1
                next_pos[cur_pos] = -1
                cur_pos = nextp
            else:
                prevp = prev_pos[cur_pos]
                nextp = next_pos[cur_pos]
                next_pos[prevp] = nextp
                prev_pos[nextp] = prevp
                prev_pos[cur_pos] = -1
                next_pos[cur_pos] = -1
                cur_pos = nextp
        elif c == "Z":
            recover, left, right = removed.pop()
            is_exist[recover] = True
            if left != -1:
                next_pos[left] = recover
            if right != -1:
                prev_pos[right] = recover
            next_pos[recover] = right
            prev_pos[recover] = left
        elif c[0] == "D":
            _, num = c.split()
            for _ in range(int(num)):
                cur_pos = next_pos[cur_pos]
        else:
            _, num = c.split()
            for _ in range(int(num)):
                cur_pos = prev_pos[cur_pos]
    result = ""
    for e in is_exist:
        if e:
            result += "O"
        else:
            result += "X"
    return result