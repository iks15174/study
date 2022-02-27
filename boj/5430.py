import sys

input = sys.stdin.readline

t = int(input())
for i in range(t):
    # 입력을 받는다.
    operation = input().strip()
    length = int(input().strip())
    num_list = input().strip().replace("[", "").replace("]", "").split(",")
    nums = [num_list[j] for j in range(length)]

    # operation의 순서에 따라 연산을 한다.
    early_finished = False
    isFront = True
    for op in operation:
        if op == "R":
            isFront = not isFront
        elif op == "D":
            if len(nums) == 0:
                print("error")
                early_finished = True
                break
            if isFront:
                nums.pop(0)
            else:
                nums.pop()

    if not early_finished:
        if not isFront:
            nums.reverse()
        print("[" + ",".join(nums) + "]")
