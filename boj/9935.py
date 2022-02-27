text = input()
boom_text = list(input())
stack = []

for t in text:
    stack.append(t)
    if len(stack) >= len(boom_text) and stack[-len(boom_text) :] == boom_text:
        for j in range(len(boom_text)):
            stack.pop()

if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))
