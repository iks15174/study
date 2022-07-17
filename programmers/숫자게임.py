def solution(A, B):
    answer = 0
    A = sorted(A)
    B = sorted(B)
    length = len(A)
    cur_a = length - 1
    cur_b = length - 1
    while cur_a >= 0 and cur_b >= 0:
        if A[cur_a] < B[cur_b]:
            answer += 1
            cur_a -= 1
            cur_b -= 1
        else:
            cur_a -= 1
    return answer