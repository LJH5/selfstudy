T = int(input())
for tc in range(1, T+1):
    result = 0
    stack = []

    for i in input():
        # '('가 입력되면 stack에 저장
        if i == '(':
            stack.append(i)
        # ')'가 입력되면 stack에 저장되어 있는 '(' pop
        elif i == ')':
            # '(' 없이 ')'오면
            if len(stack) == 0:
                result = -1
                break
            stack.pop()
    else:
        # stack에 남은 게 없으면 1 아니면 -1
        if len(stack) == 0:
            result = 1
        else:
            result = -1

    print(f'#{tc} {result}')