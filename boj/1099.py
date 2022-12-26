import math
import sys

input = sys.stdin.readline

sentence = input().strip()
n = int(input().strip())
words = [input().strip() for _ in range(n)]
dp = [-2] * len(sentence)

def calculate_cost(s1, s2):
    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)
    if sorted_s1 != sorted_s2:
        return -1
    cost = 0
    for w1, w2 in zip(s1, s2):
        if w1 != w2:
            cost += 1
    return cost
    
def solve(start_index):
    global sentence, words, dp
    if start_index >= len(sentence):
        return 0
    if dp[start_index] != -2:
        return dp[start_index]
    dp_val = math.inf
    for w in words:
        if len(w) + start_index > len(sentence):
            continue
        sub_sentence = sentence[start_index : start_index + len(w)]
        cost = calculate_cost(w, sub_sentence)
        if cost != -1:
            solve_cost = solve(start_index + len(w))
            if solve_cost != -1:
                dp_val = min(dp_val, cost + solve_cost)
    if dp_val != math.inf:
        dp[start_index] = dp_val
    else:
        dp[start_index] = -1
    return dp[start_index]

print(solve(0))