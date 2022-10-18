# 반복문자 지우기
T = int(input())
for tc in range(1, T+1):
    stack = []
    input_data = input()

    for i in input_data:
        if len(stack) == 0:         # 스택이 비어있으면
            stack.append(i)         # 그냥 넣기
        else:
            comp = stack.pop()      # 스택에서 이전에 넣은 것을 꺼냄
            if i != comp:           # 값을 비교해 같지 않으면
                stack.append(comp)  # 꺼낸 요소 다시 넣기
                stack.append(i)     # 입력 받은 요소 넣기
    result = len(stack)

    print(f'#{tc} {result}')