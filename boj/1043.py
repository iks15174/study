people, party = map(int, input().split())
party_list = [[] for _ in range(party)]
people_know = list(map(int, input().split()))
people_know_num = people_know[0]
people_know = set(people_know[1:])

roots = [i for i in range(0, people + 1)]
for know in people_know:
    roots[know] = 0


def find_root(val):
    if roots[val] == val:
        return val
    roots[val] = find_root(roots[val])
    return roots[val]


def union(val1, val2):
    val1_root = find_root(val1)
    val2_root = find_root(val2)

    if val2_root < val1_root:
        roots[val1_root] = val2_root
    else:
        roots[val2_root] = val1_root


for i in range(party):
    temp = list(map(int, input().split()))
    party_list[i] = temp[1:]  # 전체 인원수를 제외하고 저장한다.

    if len(party_list[i]) > 1:
        for j in range(1, len(party_list[i])):
            union(party_list[i][j - 1], party_list[i][j])

ans = 0
for p in party_list:
    is_possible = True
    for attend in p:
        if find_root(attend) == 0:
            is_possible = False

    if is_possible:
        ans += 1

print(ans)
