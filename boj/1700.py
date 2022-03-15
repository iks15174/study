from collections import deque

whole_num, connect_num = map(int, input().split())
connect_order = deque((map(int, input().split())))
multi_tab = [0] * whole_num
result = 0

while connect_order:
    electric_stub = connect_order.popleft()
    inserted = False
    for idx, space in enumerate(multi_tab):
        if space == 0 or space == electric_stub:  # 빈공간을 발견했거나, 이미 꽂혀있을 경우
            multi_tab[idx] = electric_stub
            inserted = True
            break

    if not inserted:  # 멀티탭에 넣을 자리가 없을 땐, 가장 나중에 바뀌는 걸 빼고 넣어준다.
        replace_idx = -1
        future_appear_idx = -1
        for idx, connected_electric in enumerate(multi_tab):
            try:
                latest_appear = connect_order.index(
                    connected_electric
                )  # 현재 꽂혀있는 기기가 나중에 또 언제 사용되는지 확인
            except:
                replace_idx = idx
                break

            if latest_appear > future_appear_idx:
                future_appear_idx = latest_appear
                replace_idx = idx
        result += 1
        multi_tab[replace_idx] = electric_stub

print(result)
