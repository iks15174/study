def solution(a, b, g, s, w, t):
    left = 1
    right = (10 ** 9) * 2 * (10 ** 5) * 2
    city_num = len(s)
    while left < right:
        time = (left + right) // 2
        stone_max = 0
        gold_max = 0
        silver_max = 0
        for i in range(city_num):
            iter_num = time // (t[i] * 2) + ((time % (t[i] * 2)) // t[i])
            stone_max += min(iter_num * w[i], g[i] + s[i])
            gold_max += min(iter_num * w[i], g[i])
            silver_max += min(iter_num * w[i], s[i])
        if stone_max >= (a + b) and gold_max >= a and silver_max >= b:
            right = time
        else:
            left = time + 1
    return right