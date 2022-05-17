import sys
import math

"""
설명
모든 점의 pair를 확인하면 시간초과가 발생한다.
빠르게 해결하기 위해 divide & conquer을 사용한다.
점을 x 축 기준으로 정렬 후 오른쪽 점들의 최소 거리와 왼쪽 거리의 최소 거리를 구한다.
구후 오른쪽과 왼쪽의 최소 거리와 가운데 선을 지나며 만들어 질 수 있는 거리 중 최소를 return하면 된다.
오른쪽 왼쪽 둘 중의 최소 거리를 d라 하면
가운데 선을 지나는 두 점들은 d 범위에 있는 것만 비교하면 된다.
"""
input = sys.stdin.readline
n = int(input().strip())
dots = []
for _ in range(n):
    x, y = map(int, input().strip().split())
    dots.append([x, y])
dots = sorted(dots)


def dist(arr1, arr2):
    return (arr1[0] - arr2[0]) ** 2 + (arr1[1] - arr2[1]) ** 2


def get_minimum_dist(sub_dots):
    if len(sub_dots) <= 3:
        minval = math.inf
        for i in range(len(sub_dots)):
            for j in range(i + 1, len(sub_dots)):
                minval = min(minval, dist(sub_dots[i], sub_dots[j]))
        return minval
    mid = len(sub_dots) // 2
    x_line = (sub_dots[mid - 1][0] + sub_dots[mid][0]) // 2
    d = min(get_minimum_dist(sub_dots[0:mid]), get_minimum_dist(sub_dots[mid:]))
    contained_dot = []
    for dot in sub_dots:
        if abs(dot[0] - x_line) ** 2 >= d:
            continue
        contained_dot.append(dot)
    contained_dot = sorted(contained_dot, key=lambda i: i[1])  # y 오름차순으로 정렬
    for i in range(len(contained_dot)):
        for j in range(i + 1, len(contained_dot)):
            if abs(contained_dot[i][1] - contained_dot[j][1]) ** 2 >= d:
                break
            d = min(d, dist(contained_dot[i], contained_dot[j]))
    return d


print(get_minimum_dist(dots))
