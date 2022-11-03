# def solution(food_times, k):
#     sorted_f = sorted(food_times)
#     prev_k = 0
#     cur_len = len(food_times)
#     cur_time = 0
#     for sf in sorted_f:
#         if sf > prev_k:
#             if cur_time + cur_len * abs(prev_k - sf) > k:
#                 break
#             cur_time += cur_len * abs(prev_k - sf)
#             prev_k = sf
#             cur_len -= 1
#         elif sf == prev_k:
#             cur_len -= 1
#     if cur_len == 0:
#         return -1
#     cur_time += cur_len * ((k - cur_time) // cur_len)
#     for idx, f in enumerate(food_times):
#         if f > prev_k and cur_time == k:
#             return idx + 1
#         if f > prev_k:
#             cur_time += 1
#     return -1


def solution(food_times, k):
    sorted_food = sorted([[val, idx + 1] for idx, val in enumerate(food_times)], reverse = True)
    food_len = len(food_times)
    eat_food = 0
    while sorted_food:
        if sorted_food[-1][0] > eat_food:
            if k >= (sorted_food[-1][0] - eat_food) * food_len:
                k -= ((sorted_food[-1][0] - eat_food) * food_len)
                eat_food += (sorted_food[-1][0] - eat_food)
                sorted_food.pop()
                food_len -= 1
            else:
                break
        else:
            food_len -= 1
            sorted_food.pop()
    if len(sorted_food) == 0:
        return -1
    k %= food_len
    sorted_idx = sorted(sorted_food, key = lambda x : x[1])
    return sorted_idx[k][1]
        