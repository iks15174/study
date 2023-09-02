import math

"""
temperature: 실외온도
t1 ~ t2: 희망온도
a: 에어컨 온도가 실내와 다를 때 소비 전력
b: 에어컨 온도가 실내와 같을 때 소비 전려
onboard: 사용자 탑승 여부
"""


def solution(temperature, t1, t2, a, b, onboard):
    answer = math.inf
    dp = [[math.inf] * len(onboard) for _ in range(51)]
    dp[to_index(temperature)][0] = 0
    temper_direction = [1, 0, -1]

    for time, is_user_exist in enumerate(onboard):
        start_temper, end_temper = get_target_temperature(is_user_exist, t1, t2)
        for appropriate_temper in range(start_temper, end_temper + 1):
            for direction in temper_direction:
                from_temper = appropriate_temper + direction
                
                if from_temper < -10 or from_temper > 40 or time == 0:
                    continue
                
                if dp[to_index(from_temper)][time - 1] == math.inf:
                    continue

                target_electric_use = dp[to_index(from_temper)][
                    time - 1
                ] + electric_use(from_temper, appropriate_temper, temperature, a, b)

                dp[to_index(appropriate_temper)][time] = min(
                    dp[to_index(appropriate_temper)][time], target_electric_use
                )
                

    for temper in range(51):
        answer = min(answer, dp[temper][len(onboard) - 1])
    return answer


def get_target_temperature(is_user_exist, t1, t2):
    if is_user_exist:
        return (t1, t2)
    else:
        return (-10, 40)


def to_index(temperature):
    return temperature + 10


def electric_use(fr, to, temperature, a, b):
    if fr < to:  # 온도가 높아져야 하는 경우
        if to <= temperature:
            return 0
        else:
            return a
    elif fr > to:  # 온도가 낮아져야 하는 경우
        if to >= temperature:
            return 0
        else:
            return a
    else:  # 온도가 유지되어야 하는 경우
        if temperature == to:
            return 0
        else:
            return b
        
print(solution(28, 18, 26, 10, 8, [0, 0, 1, 1, 1, 1, 1]))
