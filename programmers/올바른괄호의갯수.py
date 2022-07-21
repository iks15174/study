answer = 0
def solve(left, right, stack):
    global answer
    if left == 0 and right == 0 and len(stack) == 0:
        answer += 1
        return
    if left > 0:
        stack.append("(")
        solve(left - 1, right, stack)
        stack.pop()
    if right > 0 and len(stack) > 0 and stack[-1] == "(":
        stack.pop()
        solve(left, right - 1, stack)
        stack.append("(")
def solution(n):
    global answer
    left = n
    right = n
    solve(left, right, [])
    return answer
    