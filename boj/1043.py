people, party = map(int, input().split())
party_list = [[] for _ in range(party)]
people_know = list(map(int, input().split()))
people_know_num = people_know[0]
people_know = set(people_know[1:])

for i in range(party):
    temp = list(map(int, input().split()))
    party_list[i] = temp[1:]  # 전체 인원수를 제외하고 저장한다.


while True:
    prev_set_len = len(people_know)
    for p in party_list:
        for attendance in p:
            if attendance in people_know:
                people_know.update(p)
                break

    if prev_set_len == len(people_know):  # 더이상 update할 게 없을때
        break

ans = 0
for p in party_list:
    find = False
    for attendance in p:
        if attendance in people_know:
            find = True
            break
    if not find:
        ans += 1
print(ans)
