import sys

"""
풀이 
DFS를 이용해 CYCLE을 확인하는 문제이다. 방문되지 않은 노드를 타고 내려가다가 방문한 지점을 만난다.
다시 방문된 곳을 만난다는건 CYCLE 발생을 의미할 수도 있고, 이전 방문노드를 의미할 수도 있다.
CYCLE인지 확인하기 위해 이전 작업에서 체크한 곳이지 finished 배열을 통해 확인한다.
finished가 False이면 이번에 새로생긴 CYCLE이므로 team원을 확인한다.
finished가 True이면 이전에 작업에서 확인한 CYCLE이기 때문에 현재 방문 노드만 finished True로 변경하고
마무리한다.
"""
sys.setrecursionlimit(10 ** 9)
t = int(input())
have_team = 0


def dfs(cur_student):
    global student_select, visited, finished, have_team
    visited[cur_student] = True
    next = student_select[cur_student] - 1
    if not visited[next]:
        dfs(next)
    elif not finished[next]:
        cur = student_select[next] - 1
        while cur != next:
            have_team += 1
            cur = student_select[cur] - 1
        have_team += 1
    finished[cur_student] = True


for _ in range(t):
    n = int(input())
    student_select = list(map(int, input().split()))
    visited = [False] * n
    finished = [False] * n
    have_team = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)

    print(n - have_team)
