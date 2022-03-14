# 문제
# 연인 코니와 브라운은 광활한 들판에서 ‘나 잡아 봐라’ 게임을 한다. 이 게임은 브라운이 코니를 잡거나, 코니가 너무 멀리 달아나면 끝난다. 게임이 끝나는데 걸리는 최소 시간을 구하시오.
#
# 조건
# 코니는 처음 위치 C에서 1초 후 1만큼 움직이고, 이후에는 가속이 붙어 매 초마다 이전 이동 거리 + 1만큼 움직인다. 즉 시간에 따른 코니의 위치는 C, C + 1, C + 3, C + 6, …이다.
# 브라운은 현재 위치 B에서 다음 순간 B – 1, B + 1, 2 * B 중 하나로 움직일 수 있다.
# 코니와 브라운의 위치 p는 조건 0 <= x <= 200,000을 만족한다.
# 브라운은 범위를 벗어나는 위치로는 이동할 수 없고, 코니가 범위를 벗어나면 게임이 끝난다.
# 입력 형식
# 표준 입력의 첫 줄에 코니의 위치 C와 브라운의 위치 B를 공백으로 구분하여 순서대로 읽는다.
#
# 출력 형식
# 브라운이 코니를 잡을 수 있는 최소시간 N초를 표준 출력한다. 단 브라운이 코니를 잡지 못한 경우에는 -1을 출력한다.


def solve(conyPos, brownPos):
    time = 0
    visited = [[False] * 2 for _ in range(200001)]
    queue = []
    queue.append((brownPos, 0))  # 브라운의 위치와 그 위치의 시간을 의미한다.

    while 1:
        conyPos += time
        if visited[conyPos][time % 2]:
            return time
        if conyPos > 200000:
            return -1

        while queue:
            brownCurPos, time = queue.pop()
            newTime = (time + 1) % 2

            newPos = brownCurPos + 1
            if newPos >= 0 and not visited[newPos][newTime]:
                visited[newPos][newTime] = True
                queue.append((newPos, newTime))

            newPos = brownCurPos - 1
            if newPos >= 0 and not visited[newPos][newTime]:
                visited[newPos][newTime] = True
                queue.append((newPos, newTime))

            newPos = brownCurPos * 2
            if newPos >= 0 and not visited[newPos][newTime]:
                visited[newPos][newTime] = True
                queue.append((newPos, newTime))

        time += 1
