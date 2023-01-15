n = int(input())

for _ in range(n):
    stack = []
    text = list(input())
    for i in text:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
                break

    if len(stack):
        print('NO')
    else:
        print('YES')