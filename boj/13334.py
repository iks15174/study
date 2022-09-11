'''
이건 진짜 내 머리로 한번에 아이디어를 떠올리 수 없을것 같아서 기록한다.
내가 처음에 접근했던 방법은 start 시간을 기준으로 정렬한 후 정렬된 것들을 
차례로 넣다가 총 길이가 d를 넘어가면 다시 d이하로 줄어들 때 까지 앞에서 
제거해주는 방식을 deque 자료구조를 이용해서 빼주었다.
하지만 이 방법의 문제점은 address[i]가 들어왔을 땐 d 초과가 되다가 address[i + 1] 들어올 땐
d 이하가 되는 경우가 발생한다는 것이다. cur_a의 일관성이 유지되지 않는다?

풀이는 end 시간을 기준으로 정렬한 후 나머지는 위와 비슷한다.
d 길이가 초과되면 start 시간이 가장 작은 녀석을 차례차례 제거해준다.
이 방법은 address[i]일 때 d 초과가 된다면 address[i + 1]은 address[i] 보다 반드시
더 늦은 end 시간을 가지고 그러므로 i + 1 일 때도 반드시 d 초과가 발생하게 된다.
'''
import sys
import heapq

input = sys.stdin.readline
n = int(input())
address = []
for _ in range(n):
    a, b = sorted(list(map(int, input().split())))
    address.append([a, b])
d = int(input())
address = sorted(address, key = lambda x : (x[1], x[0]))
cur_a = []
ans = 0
for i in range(n):
    if address[i][1] - address[i][0] <= d:
        while cur_a:
            min_start_p = heapq.heappop(cur_a)
            if address[i][1] - min_start_p[0] <= d:
                heapq.heappush(cur_a, min_start_p)
                break
        heapq.heappush(cur_a, address[i])
        ans = max(ans, len(cur_a))
        
print(ans)