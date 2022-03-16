gear1 = list(input())
gear2 = list(input())
gear3 = list(input())
gear4 = list(input())
gear_total = [gear1, gear2, gear3, gear4]
rotate_num = int(input())


def rotate_gear(gear, direction):  # 톱니바퀴를 회전시키는 함수이다.
    if direction == 1:
        last = gear[-1]
        for i in range(len(gear) - 1):
            gear[len(gear) - 1 - i] = gear[len(gear) - 2 - i]
        gear[0] = last

    if direction == -1:
        first = gear[0]
        for i in range(len(gear) - 1):
            gear[i] = gear[i + 1]
        gear[-1] = first


for _ in range(rotate_num):
    gear_num, direction = map(int, input().split())
    gear_num -= 1
    change_list = [
        [gear_num, direction]
    ]  # 변경해야 하는 gear의 list이다. gear_num과 방향을 배열로 담는다.

    # 왼쪽에서 변경되야 하는 톱니를 확인하는 로직이다.
    cur_gear = gear_num
    cur_direction = direction
    while cur_gear > 0:
        left_gear = cur_gear - 1
        left = gear_total[left_gear]  # 왼쪽 톱니를 의미한다.
        if left[2] != gear_total[cur_gear][6]:
            change_list.append([left_gear, -cur_direction])
            cur_direction = -cur_direction
            cur_gear = left_gear

        else:
            break

    # 오른쪽에서 변경되야 하는 톱니를 확인하는 로직이다.
    cur_gear = gear_num
    cur_direction = direction
    while cur_gear < 3:
        right_gear = cur_gear + 1
        right = gear_total[right_gear]  # 왼쪽 톱니를 의미한다.
        if right[6] != gear_total[cur_gear][2]:
            change_list.append([right_gear, -cur_direction])
            cur_direction = -cur_direction
            cur_gear = right_gear

        else:
            break

    for change in change_list:
        change_gear, direction = change
        rotate_gear(gear_total[change_gear], direction)

result = 0
for idx, gear in enumerate(gear_total):
    result += int(gear[0]) * 2 ** idx
print(result)
