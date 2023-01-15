open = {'(', '['}
close = {')', ']'}
while True:
    text = input()
    stack = ['x']
    if text == '.':
        break

    for i in text:
        if i in open:
            stack.append(i)
        elif i in close:
            check = stack.pop()
            if i == ')':
                if check != '(':
                    stack.append(check)
                    stack.append(i)
            elif i == ']':
                if check != '[':
                    stack.append(check)
                    stack.append(i)
    # print(stack)
    if stack == ['x']:
        print('yes')
    else:
        print('no')