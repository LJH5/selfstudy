T = int(input())
for tc in range(1, T+1):
    result = 'error'
    arr = input().split()
    oper = {'+', '-', '*', '/'}
    stack = []
    for i in arr:
        if i == '.':                    # '.'이면 계산 종료
            if len(stack) != 1:         # 연산이 덜 끝났으면
                break
            result = stack.pop()        # 결과값 저장
        elif i not in oper:             # 연산자가 아니라면
            stack.append(i)             # stack에 넣기
        else:                           # 연산자라면
            if len(stack) < 2:
                break
            a = int(stack.pop())        # stack에서 숫자 2개를 꺼내서
            b = int(stack.pop())
            if i == '+':                # 각각의 연산 처리
                stack.append(b + a)
            elif i == '-':
                stack.append(b - a)
            elif i == '*':
                stack.append(b * a)
            else:
                stack.append(b // a)

    print(f'#{tc} {result}')