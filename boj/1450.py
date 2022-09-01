import bisect

n, c = map(int, input().split())
w = list(map(int, input().split()))
wf = w[: (n // 2)]
wb = w[(n // 2) :]


def make_sum_case(w):
    max_val = 2 ** len(w)
    result = []
    for b in range(max_val):
        idx = 0
        temp_sum = 0
        while b > 0:
            if b & 1:
                temp_sum += w[idx]
            idx += 1
            b = b >> 1
        result.append(temp_sum)
    return result


def get_middle(back_sum, fs, c):
    return bisect.bisect_right(back_sum, c - fs)


front_sum = sorted(make_sum_case(wf))
back_sum = sorted(make_sum_case(wb))

ans = 0
for fs in front_sum:
    ans += get_middle(back_sum, fs, c)
print(ans)
