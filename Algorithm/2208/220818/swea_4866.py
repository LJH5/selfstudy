# 괄호검사
def check(comp):            # 매개 변수는 여는 괄호
    if len(stack) == 0:     # 스택이 비어 있으면
        return True         # 어차피 짝을 이루지 못 하니까

    tmp = stack.pop()       # stack에서 요소를 꺼냄
    if tmp != comp:         # 맞는 여는 괄호가 아니면
        return True         # 어차피 짝을 이루지 못 하니까

T = int(input())
for tc in range(1, T+1):
    stack = []
    result = 0                          # 0으로 고정
    for data in input():
        if data == '{' or data == '(':  # 여는 괄호는
            stack.append(data)          # 스택에 넣기
        elif data == '}':               # 닫는 괄호일 때
            if check('{'):              # 짝을 못 이루면 반복문 종료
                break
        elif data == ')':               # 닫는 괄호일 때
            if check('('):              # 짝을 못 이루면 반복문 종료
                break
    else:
        if not len(stack):              # 스택이 비었다 == 괄호의 짝이 맞다
            result = 1
    print(f'#{tc} {result}')
