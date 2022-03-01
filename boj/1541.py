# 마이너스가 등장하기 전에는 더하다가 등장 이후에는 연산자 상관없이 뺴주는 것이 최소값이다.
operation = input()
num = 0
result = 0
digit = 10
minusAppeared = False
curOp = "+"
for op in operation:
    if op >= "0" and op <= "9":
        num = (num * digit) + int(op)
    if op == "-" or op == "+":
        if curOp == "-":
            if not minusAppeared:
                minusAppeared = True
            result -= num
        else:
            if not minusAppeared:
                result += num
            else:
                result -= num
        curOp = op
        digit = 10
        num = 0

if minusAppeared:
    result -= num
else:
    if curOp == "+":
        result += num
    else:
        result -= num

print(result)
