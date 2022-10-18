T = int(input())
for tc in range(1, T+1):
    result = ''
    arr = input()
    oper = ['-', '+', '*', '/']
    stack = []
    for i in arr:
        if i in oper:
            stack.append(i)
        else:
            result += i
    while stack:
        result += stack.pop()
    print(f'#{tc} {result}')