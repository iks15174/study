import sys

input = sys.stdin.readline
# 행은 먹이의 depth를 의미, i행에는 i번째의 먹이 정보가 들어있다.
# i 행의 배열은 [먹이이름, [자식 먹이 이름 배열]]의 리스트로 이루어져 있다
feed_tree = {}
n = int(input())
for _ in range(n):
    feed_info = list(input().split())
    cur_node = feed_tree
    for feed in feed_info[1:]:
        if feed not in cur_node:
            cur_node[feed] = {}
        cur_node = cur_node[feed]


def print_tree(prefix, feed_list):
    sorted_feed_list = sorted(feed_list.items(), key=lambda x: x[0])  # 먹이 이름을 기준으로 정렬
    for feed in sorted_feed_list:
        print(prefix + feed[0])
        print_tree(prefix + "--", feed_list[feed[0]])


for feed in sorted(feed_tree.items(), key=lambda x: x[0]):
    print(feed[0])
    print_tree("--", feed_tree[feed[0]])
