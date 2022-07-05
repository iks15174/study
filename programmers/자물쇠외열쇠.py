def solution(key, lock):
    key_l = len(key)
    lock_l = len(lock)
    lock_hole_num = 0
    for l in lock:
        lock_hole_num += l.count(0)
    extend_l = (key_l - 1) * 2 + lock_l
    extended_lock = [[0] * extend_l for _ in range(extend_l)]
    for i in range(key_l - 1, key_l - 1 + lock_l):
        for j in range(key_l - 1, key_l - 1 + lock_l):
            extended_lock[i][j] = lock[i - key_l + 1][j - key_l + 1]
    for _ in range(4):
        rotated_key = [[0] * key_l for _ in range(key_l)]
        for i in range(key_l):
            for j in range(key_l):
                rotated_key[i][j] = key[j][key_l - i - 1]
        key = rotated_key
        
        for r in range(extend_l - key_l + 1):
            for c in range(extend_l - key_l + 1):
                overraped = False
                fill_num = 0
                for kr in range(key_l):
                    if overraped:
                        break
                    for kc in range(key_l):
                        if key[kr][kc] == 1 and extended_lock[r + kr][c + kc] == 1:
                            overraped = True
                            break
                        elif key[kr][kc] == 1 and extended_lock[r + kr][c + kc] == 0:
                            if key_l - 1 <= r + kr <= key_l - 2 + lock_l and key_l - 1 <= c + kc <= key_l - 2 + lock_l:
                                fill_num += 1
                if not overraped and fill_num == lock_hole_num:
                    return True
        
    return False