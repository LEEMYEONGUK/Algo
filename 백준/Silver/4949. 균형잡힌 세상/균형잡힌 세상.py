while True:
    sen = input()
    if sen == ".":
        break
    stack = []

    for s in sen:
        if s in ["(", "["]:
            stack.append(s)
        elif stack and s == ")" and stack[-1] == "(":
            stack.pop()
        elif stack and s == "]" and stack[-1] == "[":
            stack.pop()
        elif s == ")":
            if not stack or stack[-1] =="[":
                print("no")
                break
        elif s == "]":
            if not stack or stack[-1] == "(":
                print("no")
                break
    else:
        if stack:
            print("no")
        else:
            print("yes")
