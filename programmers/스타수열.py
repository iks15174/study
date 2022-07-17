def solution(a):
    answer = -1
    star_record = [[] for _ in range(len(a))]
    for i in range(len(a)):
        if i - 1 >= 0 and a[i] != a[i - 1]:
            if len(star_record[a[i]]) == 0:
                star_record[a[i]].append((i, i - 1))
                continue
            else:
                if star_record[a[i]][-1][1] != i - 1:
                    star_record[a[i]].append((i, i - 1))
                    continue
        if i + 1 < len(a) and a[i] != a[i + 1]:
            star_record[a[i]].append((i, i + 1))
            continue
    for s in star_record:
        answer = max(answer, 2 * len(s))
    return answer