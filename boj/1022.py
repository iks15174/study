r1, c1, r2, c2 = map(int, input().split())
result = [[0] * ((c2 - c1) + 1) for _ in range((r2 - r1) + 1)]
cur_r = 0  # 현재 row 0
cur_c = 0  # 현재 col 0
cur_value = 1  # 회오리그리기의 현재 값이다
move_dir = [1, 1, 2, 2]  # 오른쪽, 위, 왼쪽, 아래로 이동해야 하는 칸수를 의미
move = [[0, 1], [-1, 0], [0, -1], [1, 0]]  # 오른쪽, 위, 왼쪽, 아래 이동을 의미
empty_num = ((c2 - c1) + 1) * ((r2 - r1) + 1)  # 비어 있는 칸수를 의미, 0이 되면 종료한다.
max_result = -1  # result array에서 가장 큰 값을 의미한다.

# 첫번째 값이 result 범위에 있으면 넣어준다.
if r1 <= cur_r <= r2 and c1 <= cur_c <= c2:
    result[cur_r - r1][cur_c - c1] = cur_value
    empty_num -= 1
    max_result = max(max_result, cur_value)

# board그리기 시작
def solve():
    global cur_value, cur_r, cur_c, max_result, empty_num, move_dir
    if empty_num == 0:  # 0 0 0 0을 위한 특별 조건
        return

    while True:
        for idx, dir in enumerate(move_dir):
            while dir > 0:
                cur_value += 1
                cur_r += move[idx][0]
                cur_c += move[idx][1]
                if r1 <= cur_r <= r2 and c1 <= cur_c <= c2:
                    result[cur_r - r1][cur_c - c1] = cur_value
                    empty_num -= 1
                    max_result = max(max_result, cur_value)
                    if empty_num == 0:
                        return
                dir -= 1

        move_dir = [dir + 2 for dir in move_dir]


solve()
max_num_len = len(str(max_result))
for row in result:
    formatted_row = [str(col).rjust(max_num_len) for col in row]
    print(*formatted_row)
