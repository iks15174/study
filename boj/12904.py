import sys

sys.setrecursionlimit(int(1e6))
s = input()
t = input()


def solve(t_substr):
    if t_substr == s:
        return True
    if len(t_substr) == 0:
        return False

    if t_substr[-1] == "A":
        return solve(t_substr[:-1])
    if t_substr[-1] == "B":
        # new_t_substr = list(reversed(t_substr[:-1]))
        return solve("".join(reversed(t_substr[:-1])))


print(1) if solve(t) else print(0)
