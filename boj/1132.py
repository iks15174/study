n = int(input())
words = [input() for _ in range(n)]
alphabet_cnt = {}
should_not_zero = set()
for word in words:
    should_not_zero.add(word[0])
    base = 10 ** (len(word) - 1)
    for w in word:
        if w in alphabet_cnt:
            alphabet_cnt[w] += base
        else:
            alphabet_cnt[w] = base
        base = base // 10

sorted_cnt = sorted(
    [[k, v] for k, v in alphabet_cnt.items()], key=lambda x: -x[1]
)  # (알파벳, 값)
val = 9
for sc in sorted_cnt:
    sc.append(val)
    val -= 1

if sorted_cnt[-1][0] in should_not_zero and sorted_cnt[-1][2] == 0:
    for reverse_idx in range(len(sorted_cnt) - 1, 0, -1):
        if sorted_cnt[reverse_idx][0] in should_not_zero:
            sorted_cnt[reverse_idx][2], sorted_cnt[reverse_idx - 1][2] = (
                sorted_cnt[reverse_idx - 1][2],
                sorted_cnt[reverse_idx][2],
            )
        else:
            break

ans = 0
for sc in sorted_cnt:
    ans += sc[1] * sc[2]
print(ans)
