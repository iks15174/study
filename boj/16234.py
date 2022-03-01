from collections import deque

n, l, r = map(int, input().split())
country_population = [[] for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
line_open = [[[] for _ in range(n)] for _ in range(n)]  # 서로 연결된 나라를 의미한다. y, x로 저장
move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
day = 0  # 며칠이 흘렀는지 의미함

# 국경 오픈 여부를 확인하는 함수이다.
def check_open():
    isConnected = False
    for i in range(n):
        for j in range(n):
            for m in move:
                next_x = j + m[0]
                next_y = i + m[1]
                if next_x >= 0 and next_x < n and next_y >= 0 and next_y < n:
                    diff = abs(
                        country_population[i][j] - country_population[next_y][next_x]
                    )
                    if diff >= l and diff <= r:  # 두나라의 인구 차이가 l명 이상 r명 이하일 경우
                        line_open[i][j].append((next_y, next_x))
                        line_open[next_y][next_x].append((i, j))
                        isConnected = True
    return isConnected  # 하나라도 열려 있으면 참을 반환


def bfs(pos):  # pos y, x 정보를 저장하고 있음
    queue = deque()
    queue.append(pos)
    union_country = []

    while queue:
        q = queue.popleft()
        if not visited[q[0]][q[1]]:
            visited[q[0]][q[1]] = True
            union_country.append(q)  # 방문된 연합국 추가
            for connected_country in line_open[q[0]][q[1]]:  # 현재 연합국과 연결된 연합국도 후보로 올려둠
                queue.append(connected_country)

    # 연합국의 평균 인구 수 개산
    sum = 0
    for country in union_country:
        sum += country_population[country[0]][country[1]]
    avg = sum // len(union_country)

    # 연합국의 인구를 평균으로 업데이트
    for country in union_country:
        country_population[country[0]][country[1]] = avg


# 각 나라의 인구수 입력을 받는다.
for i in range(n):
    line = list(map(int, input().split()))
    country_population[i] = line

while True:
    if check_open():
        for i in range(n):
            for j in range(n):
                if not visited[i][j]:  # 각 나라를 돌며 방문하지 않았을 경우 -> bfs를 수행한다.
                    bfs((i, j))
    else:
        break

    # 초기화 작업 & 날짜 추가
    line_open = [[[] for _ in range(n)] for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    day += 1

print(day)
