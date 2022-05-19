expression = list(input())
s = []
result = ""
for e in expression:
    if e.isupper():
        result += e
    else:
        if e == "+" or e == "-":
            while s:
                if s[-1] == "(":
                    break
                else:
                    result += s.pop()
            s.append(e)
        elif e == "/" or e == "*":
            while s:
                if s[-1] == "(" or s[-1] == "+" or s[-1] == "-":
                    break
                elif s[-1] == "*" or s[-1] == "/":
                    result += s.pop()
            s.append(e)
        elif e == "(":
            s.append(e)
        elif e == ")":
            while s[-1] != "(":
                result += s.pop()
            s.pop()
while s:
    result += s.pop()
print(result)
