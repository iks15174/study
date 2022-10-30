# def solution(a, b, g, s, w, t):
#     left = 1
#     right = (10 ** 9) * 2 * (10 ** 5) * 2
#     city_num = len(s)
#     while left < right:
#         time = (left + right) // 2
#         stone_max = 0
#         gold_max = 0
#         silver_max = 0
#         for i in range(city_num):
#             iter_num = time // (t[i] * 2) + ((time % (t[i] * 2)) // t[i])
#             stone_max += min(iter_num * w[i], g[i] + s[i])
#             gold_max += min(iter_num * w[i], g[i])
#             silver_max += min(iter_num * w[i], s[i])
#         if stone_max >= (a + b) and gold_max >= a and silver_max >= b:
#             right = time
#         else:
#             left = time + 1
#     return right

def solution(a, b, g, s, w, t):
    left = 0
    right = ((a + b) // min(w) + 1) * 2 * max(t)
    while left < right:
        max_stone = 0
        max_gold = 0
        max_silver= 0
        mid = (left + right) // 2
        for i in range(len(g)):
            send_cnt = (mid // (2 * t[i]))
            send_cnt += (1 if mid % (2 * t[i]) >= t[i] else 0)
            send_weight = send_cnt * w[i]
            max_stone += min(send_weight, g[i] + s[i])
            max_gold += min(send_weight, g[i])
            max_silver += min(send_weight, s[i])
        if max_stone >= a + b and max_gold >= a and max_silver >= b:
            right = mid
        else:
            left = mid + 1
    return left
        
            